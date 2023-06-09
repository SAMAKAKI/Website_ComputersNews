from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView

def index(request):
    context = {
        'news': News.objects.order_by('-date')
    }
    return render(request, 'news/index.html', context)

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create.html'
    form_class = NewsForm

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = '/news/'

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Error in form'

    form = NewsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', context)