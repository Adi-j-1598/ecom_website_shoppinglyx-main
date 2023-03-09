from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # CATERGORY_CHOICE=(('S','seller'),
    # ('B','buyer'))
    # user_type=models.CharField(choices=CATERGORY_CHOICE,max_length=6,null=True,blank=True)
    is_seller=models.BooleanField(default=False)
    is_buyer=models.BooleanField(default=False)
