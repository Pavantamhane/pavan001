from django.db import models


class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image=models.ImageField(upload_to='product_images/',null=True, blank=True)
    
    def __str__(self):
        return self.name