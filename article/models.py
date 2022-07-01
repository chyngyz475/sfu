
from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(
    max_length=50
  )

class Article(models.Model):
  title = models.CharField(
    verbose_name="Заголовок",
    max_length=150
  )
  image = models.ImageField(
    verbose_name="Фото",
    upload_to='acticle/article/',
    width_field=None,
    height_field=None,
  )
  date = models.DateField(
    verbose_name="Время",
    null=True,
    blank=False
  )
  month = models.CharField(
    verbose_name="Месяц",
    max_length=100,
    null=True,
    blank=False
  )
  tags = models.ManyToManyField(
    'Tag'
  )
  content = models.TextField(
    verbose_name="Тест",
    max_length=1000
  )

  def __str__(self):
      return self.title
