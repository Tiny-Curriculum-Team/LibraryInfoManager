from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Reader(AbstractBaseUser):
    ReaderID = models.AutoField(primary_key=True, auto_created=True, editable=False)
    reader_name = models.CharField(max_length=40)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=1024)
    account_status = models.CharField(max_length=20)
    tel = models.CharField(max_length=11)
    trustworthiness = models.IntegerField(default=100)
    max_borrow_day = models.IntegerField(default=30)
    max_borrow_count = models.IntegerField(default=10)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = [
        "reader_name",
        "user_name",
        "password",
        "account_status",
        "tel",
        "trustworthiness",
        "max_borrow_day",
        "max_borrow_count",
    ]
    USERNAME_FIELD = 'ReaderID'
    is_anonymous = False
    is_authenticated = False

    class Meta:
        db_table = 'Reader'


class Administrator(models.Model):
    WorkID = models.IntegerField(primary_key=True)
    admin_name = models.CharField(max_length=40)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=1024)
    tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'Administrator'
