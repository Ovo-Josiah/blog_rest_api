from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
  title = models.CharField(max_length= 256)
  is_published = models.BooleanField(default = True)


class Articles(models.Model):
  title = models.CharField(max_length= 256)
  slug = models.CharField(max_length=200, null=True, unique=True)
  is_published = models.BooleanField(default = True)
  body = models.TextField()
  category = models.ForeignKey(Category, on_delete = models.DO_NOTHING)
  created_at = models.DateTimeField(auto_now_add= True)
  updated_at = models.DateTimeField(auto_now= True)

  # Assignment: add slug field to this article model

  def save(self, *args, **kwargs):
    self.slug = self.createslug
    super(Category, self).save(self, *args, **kwargs)

  def createslug(self):
    return slugify(self.title)

  