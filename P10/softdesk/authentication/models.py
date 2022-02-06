from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)