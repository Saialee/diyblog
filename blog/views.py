from django.shortcuts import render
from .models import Blogger, BlogPost, Comment

# Create your views here.

#Home Page View
def index(request):
    
     # Generate counts of some of the main objects
    num_blogs = BlogPost.objects.all().count()
    num_bloggers = Blogger.objects.all().count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers
    }


    return render(request, "index.html", context=context)