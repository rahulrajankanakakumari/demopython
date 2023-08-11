from django.urls import reverse_lazy

from.forms import TodoForm
from django.shortcuts import render, redirect
from.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView




class TaskUpdateviews(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class TaskDetailviews(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskListviews(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

# Create your views here.
def add (request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('text','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url= reverse_lazy('cbvhome')

# def details(request):
#     task=Task.objects.all()
#     return render(request,'detail.html',{'task':task})

def delete (request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')

def update (requwst,id):
    task=Task.objects.get(id=id)
    f=TodoForm(requwst.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(requwst,'edit.html',{'f':f,'task':task})