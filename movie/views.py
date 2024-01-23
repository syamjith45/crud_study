from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from . models import Movie
from . forms import MovieForm
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("created")
    else:
        form=MovieForm()
        
    return render(request,'Movie_record.html',{'form':form})


def list(request):
    record=Movie.objects.all()
    
    return render(request,'list_record.html',{'records':record})

def edit(request,pk):
    records=get_object_or_404(Movie,pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST,instance=records)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("updated")
    else:
        form=MovieForm(instance=records)
    
    return render(request,'edit_records.html',{'form':form})


def delete_record(request,pk):
    record=get_object_or_404(Movie,pk=pk)
    record.delete()
    return HttpResponse('delete')
    