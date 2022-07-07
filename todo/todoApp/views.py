from django.shortcuts import render, redirect
from .forms import todoForm
from .models import todo

# Create your views here.

def index(request):
	form = todoForm()
	todolist = todo.objects.all()

	if request.method == 'POST':
		form = todoForm(request.POST)
		if form.is_valid():
			form.save()
			redirect('/')


	return render(request, 'todoApp/index.html', {'form':form, 'todolist':todolist})
