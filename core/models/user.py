from django.contrib.auth.models import AbstractUser as BaseUser

class User(BaseUser):
    def __str__(self):
        return self.username
