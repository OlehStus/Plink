from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MyUser(models.Model):

    email = models.EmailField(max_length=100, verbose_name='Email')
    password = models.CharField(max_length=16, verbose_name='Password')
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)




