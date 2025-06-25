from django.db import models
from django.contrib.auth.models import AbstractUser

ACTIVITY_CHOICES = (
    ('call', "Call"),
    ('meeting', "Meeting"),
    ('email', "Email")
)

# Create your models here.
class User(AbstractUser):

    def __str__(self):
        return f"{self.id} . {self.username}"
    
    def check_permission(self, obj):
        return self == obj.user
    
class Contact(models.Model):
    name = models.CharField(max_length=40, blank=True)
    surname = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    company = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self) -> str:
        return f"#{self.id} . {self.name}"


class Activity(models.Model):
    name = models.CharField(max_length=40, blank=True)
    date = models.DateTimeField(auto_now=True)
    activity_type = models.CharField(max_length=10, choices=ACTIVITY_CHOICES)
    description = models.CharField(max_length=70, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='activities')

    def __str__(self) -> str:
        return f"#{self.id} . {self.name}"

