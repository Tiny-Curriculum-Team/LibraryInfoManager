from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, admin_name, user_name, password, tel):
        if not tel:
            raise ValueError('Users must have an tele number.')

        user = self.model(
            WorkID=1,
            admin_name=admin_name,
            user_name=user_name,
            tel=tel,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


# Create your models here.
class Administrator(AbstractBaseUser):
    WorkID = models.AutoField(primary_key=True, auto_created=True, editable=False)
    admin_name = models.CharField(max_length=40)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=1024)
    tel = models.CharField(max_length=11)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = [
        "admin_name",
        "user_name",
        "password",
        "tel",
    ]
    USERNAME_FIELD = 'WorkID'
    is_anonymous = False
    is_authenticated = False

    class Meta:
        db_table = 'Administrator'
