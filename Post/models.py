from django.db import models
from User.models import User

# Create your models here.
class Post(models.Model):
  user = models.ForeignKey(User, 
                           on_delete=models.CASCADE, 
                           related_name="posts", 
                           related_query_name="posts",
                           db_index=True)
  content = models.TextField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  class Meta:
    db_table = "posts"

