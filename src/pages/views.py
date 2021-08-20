from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category, Tag
from product.models import Product

# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)
    # return HttpResponse("<h1>Hey home</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):  # *args, **kwargs
    # return HttpResponse("<h1>Contact</h1>") # string of HTML code
    post_list = Post.objects.all().order_by('-created_time')
    tag_list = Tag.objects.all()
    return render(request, "contact.html",
     context={'post_list': post_list,
              'tag_list': tag_list,}
     )

def about_view(request, *args, **kwargs):  # *args, **kwargs
    # return HttpResponse("<h1>About</h1>") # string of HTML code
    my_context = {
        "my_text": "This is about me",
        "my_number": 996

    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):  # *args, **kwargs
    # return HttpResponse("<h1>Social</h1>") # string of HTML code
    return render(request, "social.html", {})
