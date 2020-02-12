from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=50, unique=True)
  password = models.CharField(max_length=50)
  avatar = models.FileField(blank=True)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  class Meta:
    db_table = "users"
    ordering = ["name"]

