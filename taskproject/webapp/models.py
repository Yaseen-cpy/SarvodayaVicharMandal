from django.db import models

# Create your models here.


from django.db import models

class Stories(models.Model):
    news = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')




    def __str__(self):
        return self.news
