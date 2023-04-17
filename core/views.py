from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.


def index(request):
    if request.method == 'POST':
        task = request.POST['task']
        prior = request.POST['prior']
        date=request.POST['date']
        task = Task(
            name=task,
            priority=prior,
            date=date
        )
        task.save()
    tasks=Task.objects.all().order_by('priority')
    return render(request, 'base.html',{'task':tasks})

def delete(request,id):
    task=Task.objects.get(id=id)
    print(task)
    task.delete()
    return redirect('index')



def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request,'update.html',{'form':form})


