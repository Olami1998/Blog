from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post, Category
from blog.forms import NewsForm


# Create your views here.

def frontpage(request):
    post_list = Post.objects.filter(status=Post.ACTIVE)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cat = Category.objects.all()
    
    
    if request.method == "POST":
        form = NewsForm(request.POST)
        
        if form.is_valid():
            news = form.save(commit=False)
            news.post
            news.save()
    
    return render(request, 'core/frontpage.html', {'page_obj': page_obj, 'cat':cat})



def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')