from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Add_to_Task


def home(request):
    return render(request, "index.html")


def add_task(request):
    if request.method == "POST":
        try:
            # Get form data
            title = request.POST.get("title")
            content = request.POST.get("content")
            status = request.POST.get("status")
            image = request.FILES.get("image")  # For file uploads
            
            # Create new task
            task = Add_to_Task.objects.create(
                title=title,
                content=content,
                profile=image,  
                status=status,
                user=request.user
            )
            messages.success(request, "Task added successfully!")
            return redirect('home') 
            
        except Exception as e:
            messages.error(request, f"Error adding task: {str(e)}")
            return redirect('add_task') 
    
    return render (request,"Add_Task.html")


def ShowTask(request):
    ShowTask=Add_to_Task.objects.all().order_by("-created_at")
    return render (request,"ShowTask.html",{"showTask":ShowTask})