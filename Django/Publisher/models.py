from django.db import models


# Create your models here.
class Publisher(models.Model):
    PublisherID = models.AutoField(primary_key=True, auto_created=True, editable=False)
    publisher_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'Publisher'

