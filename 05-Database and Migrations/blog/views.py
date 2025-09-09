from django.shortcuts import render
from django.http import HttpResponse



# create posts 

posts = [
    {
        'author': 'Ujjwal',
        'title': 'Algorithms Practice',
        'content': 'Two-pointer patterns, sliding window , greedy approaches.',
        'date_posted': 'September 06, 2025'
    },
    {
        'author': 'Rudra',
        'title': 'Django Views Explained',
        'content': 'Function-based vs class-based views with simple URL routing examples.',
        'date_posted': 'September 06, 2025'
    },
    {
        'author': 'Aashiq',
        'title': 'Networking 101',
        'content': 'OSI layers, TCP vs UDP, Routing.',
        'date_posted': 'September 06, 2025'
    }
]







# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html',context)
#  return render(request, 'home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def name(request):
    return HttpResponse('<h1>Hiii  I am Ujjwal Kamila ,Python Developer</h1>')

