from django.db import models


# Create your models here.
class Borrow(models.Model):
    OperationID = models.AutoField(primary_key=True, auto_created=True, editable=False)
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book.Book', on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, default="未归还")
    give_back_time = models.DateTimeField()

    class Meta:
        db_table = 'Borrow'

