from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return redirect('/shows/new')

def new(request):
    return render(request, 'new.html')

def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def create_show(request):
    if request.method == 'POST':
        new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
        print(new_show)
        return redirect('/shows')
    return redirect('/shows/new')

def one_show(request, id):
    context = {
        'viewed_show': Show.objects.get(id=id)
    }
    return render(request, 'one_show.html', context)

def show_edit_page(request, id):
    context = {
        'edit_show': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def process_edit(request, id):
    if request.method == 'POST':
        str_id = str(id)
        edit_show = Show.objects.get(id=id)
        edit_show.title = request.POST['title']
        edit_show.network = request.POST['network']
        edit_show.release_date = request.POST['release_date']
        edit_show.desc = request.POST['desc']
        edit_show.save()
        return redirect(f'/shows/{{show.id}}')
    return redirect('/')

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')