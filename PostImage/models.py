from django.db import models
from Post.models import Post

# Create your models here.
class PostImage(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                           related_name="post_images", 
                           related_query_name="post_images",
                           db_index=True)
  image = models.FileField(blank=True)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  class Meta:
    db_table = "post_images"
