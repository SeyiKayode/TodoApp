from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('date')
    context = {
        'todo_items': todo_items
    }
    return render(request, 'todo/index.html', context)
@csrf_exempt
def add_todo(request):
    content = request.POST['content']
    create_todo = Todo.objects.create(text=content)
    return redirect('home')
@csrf_exempt
def delete_todo(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect('home')
