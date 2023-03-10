from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField()
    price=models.IntegerField()

    def __str__(self):
        return self.name
    
class Card(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    number=models.IntegerField()
    total=models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
