from django.db import models

class AdminUser(models.Model):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username