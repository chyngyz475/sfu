from django.db import models

class News(models.Model):
   title = models.CharField(max_length=250)
   content = models.TextField(max_length=500)
   cteated_at = models.DateField(auto_now_add=True)
   photo = models.ImageField(upload_to='%Y/%m/%d')