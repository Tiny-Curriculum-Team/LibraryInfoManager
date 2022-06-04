from django.db import models


# Create your models here.
class Manage(models.Model):
    OperationID = models.AutoField(primary_key=True, auto_created=True, editable=False)
    WorkID = models.ForeignKey('Users.User', on_delete=models.CASCADE)
    ISBN = models.ForeignKey('Book.Book', on_delete=models.CASCADE)
    operate_type = models.CharField(max_length=20)
    operate_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Manage'

