from django.shortcuts import render , redirect
from .models import food , Sabad , Wallet , Vote
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SabadForm , WalletForm , VoteForm
from django.db.models import Sum
from django.http import HttpResponse
#from B.settings import glob_count

# Create your views here.

#this is for unique field of order_number
#glob_count = 0

def show_food(request):
    #user = User.objects.get(id = user_id)
    food_list = food.objects.all()
    context={
        'food': food_list,
        'user' : request.user
    }
    return render(request , 'index.html' , context)

def detail_food(request , food_id):
    #user = User.objects.get(id = user_id)

    food1 = food.objects.get(id = food_id)

    if request.method == 'POST':
        sabad_form = SabadForm(request.POST)
        if sabad_form.is_valid():
            cd = sabad_form.cleaned_data
            total = cd['number'] * food1.price

            if request.user.is_authenticated:
                new_sabad = Sabad(user=request.user, food=food1,number=cd['number'],total_price=total, order_number=-1)
                new_sabad.save()
            else:
                new_sabad = {'user': request.user, 'food': food1, 'number':cd['number'], 'total_price':total , 'order_number': -1 }
                request.session[0] = 'Sabad'
                request.session['Sabad'].append(new_sabad)
            messages.success(request, 'food added to cart successfully.')
            return redirect('show')

    context = {
        'food': food1,
        'user' :request.user
    }
    return render(request, 'detail.html', context)

def final_sabad(request):
    #user = user = User.objects.get(id=user_id)
    final_sabad = Sabad.objects.all().filter(user=request.user , Is_final=False)
    sum = Sabad.objects.filter(user=request.user , Is_final=False).aggregate(Sum('total_price'))

    context = {
        'final_sabad' : final_sabad,
        'sum' : sum,
        'user' : request.user
    }

    return render(request, 'finalsabad.html', context)

def pay(request , user_id):

    ordernumber = "!"
    user = User.objects.get(id=user_id)
    wallet = Wallet.objects.get(user=user)
    sabads = Sabad.objects.filter(user=user, Is_final=False)
    total = 0
    for sabad in sabads:
        total += sabad.total_price
    #sum = Sabad.objects.filter(user=user, Is_final=False).aggregate(Sum('total_price'))
    #field_object = Wallet._meta.get_field('money')
    #field_value = field_object.value_from_object(wallet)
    #field_value = getattr(wallet, wallet.money)
    #x = money.value_from_object(wallet)
    #x = wallet.money

    if total > wallet.money:
        messages.error(request, 'your money is not enough. plz recharge your wallet')
        return redirect('wallet', user_id=user.id)

    else:
        new_money = wallet.money - total
        Wallet.objects.all().filter(user=user).update(money=new_money)
        #Sabad.objects.all().filter(user=user, Is_final=False, order_number=-1).update(glob_count += 1 )
        sabad_list = Sabad.objects.all().filter(user=user, Is_final=False , order_number = -1)

        for sabad in sabad_list:
            ordernumber += str(sabad.id)
            ordernumber += "_"

        Sabad.objects.all().filter(user=user, Is_final=False, order_number=-1).update(order_number=ordernumber)
        #return HttpResponse(ordernumber)
        Sabad.objects.all().filter(user=user, Is_final=False).update(Is_final=True)

        return HttpResponse(f"paument successfully , your order number is {ordernumber}")

def cart_history(request , user_id):
    user = User.objects.get(id = user_id)
    bought_list = Sabad.objects.all().filter(user = user , Is_final=True)
    cart_list = Sabad.objects.all().filter(user = user , Is_final=False)

    context = {
        'bought_list' : bought_list,
        'cart_list' : cart_list,
        'user' : user
    }

    return render(request , 'history.html' , context)

def charge_wallet(request , user_id):
    user = User.objects.get(id=user_id)
    wallet = Wallet.objects.get(user=user)

    if request.method == 'POST':
        wallet_form = WalletForm(request.POST)
        if wallet_form.is_valid():
            cd = wallet_form.cleaned_data
            new_money = wallet.money + cd['money']
            Wallet.objects.all().filter(user=user).update(money=new_money)
            messages.success(request, 'wallet updated successfully.')
            return redirect('show', user_id=user.id)

    context = {
        'wallet' : wallet
    }

    return render(request , 'wallet.html' , context)

def cancle_order(request , user_id , order_number):
    user = User.objects.get(id=user_id)
    wallet = Wallet.objects.get(user=user)
    sabads = Sabad.objects.all().filter(user=user, order_number=order_number)
    total = 0
    for sabad in sabads:
        total += sabad.total_price

    new_money = wallet.money + total
    Wallet.objects.all().filter(user=user).update(money=new_money)
    Sabad.objects.all().filter(user=user, order_number=order_number).delete()
    messages.success(request, 'cancel order successfully')
    return redirect('show', user_id=user.id)

def show_vote(request , user_id):
    user = User.objects.get(id=user_id)
    bought_list = Sabad.objects.all().filter(user=user, Is_final=True)
    context = {
        'bought_list': bought_list,
        'user': user
    }

    return render(request, 'show_vote.html', context)

def vote(request , user_id , food_id):
    user = User.objects.get(id=user_id)
    foods = food.objects.get(id=food_id)

    if request.method == 'POST':
        vote_form = VoteForm(request.POST)
        if vote_form.is_valid():
            cd = vote_form.cleaned_data
            new_vote = Vote(user=user , food=foods , price_rate=cd['price_rate'] , behdasht_rate=cd['behdasht_rate'] , service_rate=cd['service_rate'])
            new_vote.save()
            messages.success(request, 'voted succesfully , thanks for voting')
            return redirect('show_vote', user_id=user.id)

    else:
        vote_form = VoteForm()
        return render(request, 'vote.html', {'form' : vote_form})






