from django.db import models


# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(primary_key=True, null=False, max_length=20, db_index=True)
    book_name = models.CharField(null=False, max_length=40, db_index=True)
    author = models.CharField(null=False, max_length=40, db_index=True)
    location = models.CharField(null=False, max_length=20)
    status = models.CharField(null=False, max_length=5, default='IN')
    book_type = models.ForeignKey('BookType.BookType', on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher.Publisher', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Book'


