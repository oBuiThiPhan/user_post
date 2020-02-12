from django.db import models
from Post.models import Post
from User.models import User

# Create your models here.
class Comment(models.Model):
  user = models.ForeignKey(User, 
                           on_delete=models.CASCADE, 
                           related_name="comments", 
                           related_query_name="comments",
                           db_index=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                           related_name="comments", 
                           related_query_name="comments",
                           db_index=True)
  content = models.TextField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  class Meta:
    db_table = "comments"
