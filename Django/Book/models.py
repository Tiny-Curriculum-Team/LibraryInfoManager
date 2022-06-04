from django.db import models


# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(primary_key=True, null=False, max_length=20)
    book_name = models.CharField(null=False, max_length=40)
    author = models.CharField(null=False, max_length=40)
    location = models.CharField(null=False, max_length=20)
    book_type_id = models.ForeignKey('BookType.BookType', on_delete=models.CASCADE)
    PublisherID = models.ForeignKey('Publisher.Publisher', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Book'


