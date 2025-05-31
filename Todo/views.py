from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Add_to_Task
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")

@login_required
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
                profile=image,  # Assuming CloudinaryField handles file upload
                status=status,
                user=request.user
            )
            messages.success(request, "Task added successfully!")
            return redirect('home')  # Replace 'home' with your desired redirect URL
            
        except Exception as e:
            messages.error(request, f"Error adding task: {str(e)}")
            return redirect('add_task')  # Redirect back to add task page on error
    
    # For GET requests, show the form
    return render(request, "add_task.html", {
        'status_choices': Add_to_Task.Status.choices
    })