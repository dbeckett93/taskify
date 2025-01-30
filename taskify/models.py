from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default='MEDIUM'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True
    )

    class Meta:
        app_label = 'taskify'
        ordering = ['due_date', '-priority']

    def __str__(self):
        return self.title 