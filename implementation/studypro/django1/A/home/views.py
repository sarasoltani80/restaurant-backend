from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import Todo
from django.contrib import messages
from . forms import TodoCreateForm, TodoUpdateForm

def home(request):
    all=Todo.objects.all()
    All={'todos': all}
    return render(request, 'home.html',context=All)

def say_hello(request):
    person = {'name' : 'admin'}
    return render(request , 'hello.html', context=person)  #context have to be a dictionary

#showing a html web page to user

def details(request , todo_id):
    todo = Todo.objects.get(id=todo_id)
    ToDo={'todo': todo}
    return render(request, 'detail.html' , context=ToDo)

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'todo deleted successfully')
    return redirect('/')

def create(request):
    if request.method == 'POST':
        Form = TodoCreateForm(request.POST)
        if Form.is_valid():
            cd=Form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            #messages.success(request, 'todo deleted successfully', 'success')
            return redirect('/')
    else:
        Form = TodoCreateForm()
    return render(request , 'create.html', {'form': Form})


def update(request , todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request , 'your todo updated successfully', 'success')
            return redirect('details',todo_id)
            #because it has all the information doesnt need to create again. just save it
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request , 'update.html' , {'form': form})


