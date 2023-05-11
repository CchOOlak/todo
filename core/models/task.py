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
    priority = models.IntegerField
    keywords = models.TextField(default="", blank=True)

    created_at = models.DateField(auto_now_add=True)


class TaskUser(models.Model):
    task = models.ForeignKey(Task, related_name="assigned_users", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="assigned_tasks", on_delete=models.CASCADE)
