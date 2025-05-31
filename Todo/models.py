from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Add_to_Task(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # Changed from Tittle to title
    content = models.CharField(max_length=300)
    profile = CloudinaryField('images')
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} - {self.title} - {self.status}'

  