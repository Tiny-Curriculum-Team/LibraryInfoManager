from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, name, nickname, password, tel, is_admin):
        user = self.model(
            name=name,
            nickname=nickname,
            tel=tel,
            is_admin=is_admin
        )
        user.set_password(password)
        user.save(using="default")

        return user

    def create_user(self, name, nickname, password, tel, UserID=None):
        return self._create_user(name, nickname, password, tel, False)

    def create_superuser(self, name, nickname, password, tel, UserID=None):
        return self._create_user(name, nickname, password, tel, True)


class User(AbstractBaseUser):
    UserID = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=1024)
    tel = models.CharField(max_length=11)
    # User Status Properties
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    # User Extra Properties
    trustworthiness = models.IntegerField(default=100, null=True)
    max_borrow_day = models.IntegerField(default=30, null=True)
    max_borrow_count = models.IntegerField(default=10, null=True)

    objects = UserManager()

    REQUIRED_FIELDS = [
        "name",
        "nickname",
        "password",
        "tel",
    ]
    USERNAME_FIELD = 'UserID'
    is_anonymous = False
    is_authenticated = False

    class Meta:
        db_table = 'Users'

