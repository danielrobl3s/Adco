from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": tasks})


def create_task(request):
    new_title = request.POST["title"]
    new_description = request.POST["description"]
    if new_title == "" or new_description == "":
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html", {"tasks": tasks, "error": "Title and description is required"}
        )
    task = Task(title=new_title, description=new_description)
    task.save()
    return redirect("/tasks/")


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/tasks/")


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = Task(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = Task(instance=task)
    return render(request, 'list_tasks.html', {'form': form})