from django.shortcuts import render
from django.views import generic
from .models import Blogger, BlogPost, Comment

# Create your views here.

#Home Page View
def index(request):
    
     # Generate counts of some of the main objects
    num_blogs = BlogPost.objects.all().count()
    num_bloggers = Blogger.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits


    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits
    }


    return render(request, "index.html", context=context)

#BlogPost List View
class BlogPostListView(generic.ListView):
    model = BlogPost
    template_name = "blog/blogs.html"
    context_object_name = 'allblogposts'
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    context_object_name = "blogpost"
    template_name = "blog/blogpost_detail.html"

class BloggersListView(generic.ListView):
    model = Blogger
    context_object_name = 'allbloggers'
    template_name = 'bloggers.html'
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Blogger
    context_object_name = 'blogger'
    template_name = 'blogger_detail.html'


