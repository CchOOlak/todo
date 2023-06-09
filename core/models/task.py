from django.db import models

from core.models import User

class Task(models.Model):
    title = models.CharField(max_length=500, null=False)
    description = models.TextField(default="", blank=True)
    author = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    status_enum = (
        (0, "inactive"),
        (1, "todo"),
        (2, "in progress"),
        (3, "done"),
    )
    status = models.IntegerField(choices=status_enum, default=1)
    
    priority_enum = (
        (0, "low"),
        (1, "high"),
        (2, "critical"),
    )
    priority = models.IntegerField(choices=priority_enum, default=0)

    keywords = models.TextField(default="", blank=True)
    created_at = models.DateField(auto_now_add=True)
