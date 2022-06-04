from django.db import models


# Create your models here.
class BookType(models.Model):
    BookTypeID = models.AutoField(primary_key=True, auto_created=True, editable=False)
    book_type_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'BookType'
