from django.db import models


# Create your models here.
class Reader(models.Model):
    ReaderID = models.CharField(max_length=20, primary_key=True)
    reader_name = models.CharField(max_length=40)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=1024)
    account_status = models.CharField(max_length=20)
    tel = models.CharField(max_length=11)
    trustworthiness = models.IntegerField()
    max_borrow_day = models.IntegerField()
    max_borrow_count = models.IntegerField()

    REQUIRED_FIELDS = [
        "reader_name",
        "user_name",
        "password",
        "account_status",
        "tel",
        "trustworthiness",
        "max_borrow_day",
        "max_borrow_count"
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
