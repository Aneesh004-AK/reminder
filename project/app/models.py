# models.py
from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200,default=None,null=True)
    Timer = models.DateTimeField(default=None,null=True)
    mode = models.CharField(max_length=10, choices=[('mail', 'Email',), ('sms', 'SMS'), ('both', 'Both')])
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
