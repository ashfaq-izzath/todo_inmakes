from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . forms import todo
from . models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class todolistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'tasks'

class tododetailview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task'

class todoupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})

class tododeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url =reverse_lazy('cbvhome')

def home(request):
    obj = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')

        ans=task(name=name, priority=priority,date=date)
        ans.save()

    return render(request,'home.html',{'tasks':obj})

# def details(request):
#     obj=task.objects.all()
#     return render(request,'details.html', {'tasks':obj})

def delete(request,taskid):
    task1=task.objects.get(id=taskid)
    if request.method=='POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')

def edit(request,id):
    form=task.objects.get(id=id)
    f=todo(request.POST or None, instance=form)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html', {'f':f, 'form':form})