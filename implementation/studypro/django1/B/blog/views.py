from django.shortcuts import render
from .models import Blog , Tag, Category , Comment
from .forms import CommentForm , BlogForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse

def show_blog(request):
    #user = User.objects.get(id = user_id)
    blogs = Blog.objects.all()
    paginator = Paginator(blogs , 1)
    #show 6 blogs in each w

    page_number = request.GET.get('page')
    #user enters the page number that wants and shows it in url

    blog_list = paginator.get_page(page_number)
    #returns each blog refers to each page. returns blogs for first page , second page , ...

    context = {'blog' : blog_list,
               #'user' : user
               }
    return render(request , 'show_blog.html' , context)

def detail_blog(request , blog_id):
    blog = Blog.objects.get(id = blog_id)
    tag = Tag.objects.all().filter(blog=blog)
    # blog is related name of field tags in Blog class
    recentpost = Blog.objects.all().order_by('-created_at')[:4]
    category = Category.objects.all().filter(blog=blog)
    comments = Comment.objects.all().filter(blog = blog)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_comment = Comment(blog= blog , name = cd['name'] , email = cd['email'] , message = cd['message'])
            new_comment.save()

    context = {'blog' : blog,
               'tags' : tag,
               'recent': recentpost,
               'category' : category,
               'comments' : comments,
               }
    return render(request , 'detail_blog.html' , context)

def filter_tag(request , tag):
    blogs = Blog.objects.all().filter(Tag__slug=tag)
    context = {
        'blog' : blogs
    }
    return render(request, 'show_blog.html', context)

def filter_category(request , category):
    blogs = Blog.objects.all().filter(category__slug=category)
    context = {
        'blog': blogs
    }
    return render(request, 'show_blog.html', context)

def search(request , field):

    myList = field.partition('\'')
    searchfield = myList[2]
    #return HttpResponse(myList[2])
    if request.method == 'GET':
        #if request.GET.get("search") != None:
        q = request.GET.get("search")
        if searchfield == 'title':
            blogs = Blog.objects.filter(title__icontains = q)
        if searchfield == 'content':
            blogs = Blog.objects.filter(content__icontains = q)
        if searchfield == 'description':
            blogs = Blog.objects.filter(description__icontains = q)
        #if searchfield == 'author':
         #   blogs = Blog.objects.filter(author__icontains = q)


    return render(request , 'show_blog.html' , {'blog' : blogs})

def add_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            cd = blog_form.cleaned_data
            new_blog = BlogForm(title=cd['title'], description=cd['description'], content=cd['content'], author=cd['author'], category=cd['category'] , Tag=cd['Tag'] )
            new_blog.save()

    else:
        blog_form = BlogForm()
    return render(request, 'blogform.html', {'blog_form': blog_form})







