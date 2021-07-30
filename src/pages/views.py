from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)
    # return HttpResponse("<h1>Hey home</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):  # *args, **kwargs
    # return HttpResponse("<h1>Contact</h1>") # string of HTML code
    return render(request, "contact.html", {})

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
