from django.db import models

# Create your models here.

class Comment(models.Model):
    username  = models.CharField(max_length = 50)
    comment  = models.TextField()
    first_submit = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'