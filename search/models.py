from django.db import models

# Create your models here.


class Report(models.Model):
    file_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date_added = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    program_id = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    categories =
    url = models.URLField()
