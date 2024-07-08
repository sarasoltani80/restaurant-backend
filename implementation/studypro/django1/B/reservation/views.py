from django.shortcuts import render , redirect
from . forms import ReservationForm
from .models import Reservation , Table
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import datetime as dt
import time as t
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def reserve(request):
    reserve_form = ReservationForm()
    #user = User.objects.get(id=user_id)

    if request.method == "POST":
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            cd = reserve_form.cleaned_data
            duration = int(cd['duration'])
            delta = dt.timedelta(minutes=duration)
            #t = cd['start_time'].t()
            finaltime = (dt.datetime.combine(dt.date(1, 1, 1), cd['start_time']) + delta).time()
            #finaltime = cd['start_time'] + timedelta(hours=duration)
            tables = Table.objects.all().filter(chairsnumber = cd['number'])
            #tables_copy = tables

            #reserves = Reservation.objects.all().filter(start_time__lte=cd['start_time'] , date = cd['date'])
            reserves = Reservation.objects.all().filter(date=cd['date'], start_time__lte=cd['start_time'],final_time__gt=cd['start_time'])
            bad_table_ids = []
            good_table_ids = []
            for reserve in reserves:
                bad_table_ids.append(reserve.table)

            for table in tables:
                result = bad_table_ids.count(table)
                if result == 0:
                    good_table_ids.append(table)
                    #return HttpResponse(good_table_ids)

            #good_tables = Table.objects.all().filter(Table.id in good_table_ids, chairsnumber = cd['number'])
            #for reserve in reserves:
             #   for table in tables:
              #      if reserve.table == table:
               #         table.delete()
                #        return HttpResponse('saraaa')

            if not good_table_ids:
                #return HttpResponse('there is no tables for you at this time and date. plz choose another date or time')
                messages.error(request, 'there is no tables for you at this time and date. plz choose another date or time', 'error')
                return redirect('show')

            else:
                context = {
                    'tables' : good_table_ids,
                    'user' : request.user,
                    'reserves' : reserves,
                }
                recent_reserve = Reservation(user=request.user , phone = cd['phone'] , number=cd['number'] , date=cd['date'] , start_time = cd['start_time'] , final_time=finaltime , duration = duration)
                recent_reserve.save()
                return render(request, 'table.html', context)

        else:
            return render(request, 'reservation.html',{'form' : reserve_form})

    else:
        reserve_form = ReservationForm()
        context = {'form' : reserve_form}
        return render(request , 'reservation.html' , context)

def update_table(request , user_id , tb_id):
    user = User.objects.get(id=user_id)
    table = Table.objects.get(id=tb_id)

    if not table:
        Reservation.objects.all().filter(user=user, table__isnull=True).delete()
        messages.error(request, 'You couldnt reserve the table', 'error')
        return redirect('show', user_id=user.id)

    else:
        Reservation.objects.all().filter(user=user , table__isnull=True).update(table=table)
        messages.success(request, 'You reserve the table successfully', 'success')
        return redirect('show' , user_id=user.id)


