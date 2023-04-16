from django.shortcuts import render

def index(request):
    return render(request, 'main_news/index.html')

def about(request):
    return render(request, 'main_news/about.html')

def contact(request):
    return render(request, 'main_news/contact.html')