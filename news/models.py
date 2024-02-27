from django.db import models


# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField(default="")
    
    def __str__(self) -> str:
        return self.title
