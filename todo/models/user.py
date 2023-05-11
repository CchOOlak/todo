from django.contrib.auth.models import User as BaseUser

class User(BaseUser):
    def __str__(self):
        return self.username
