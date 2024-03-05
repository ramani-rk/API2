from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    Pro_cat_id=models.IntegerField()
    Pro_cat_Name=models.CharField(max_length=100)

    def __str__(self):
        return self.Pro_cat_Name
    


class Product(models.Model):
    Pro_id=models.IntegerField(primary_key=True)
    Pro_Cat_Name=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    Pro_Name=models.CharField(max_length=100)
    Pro_Brand=models.CharField(max_length=100)
    Pro_Price=models.IntegerField()

    def __str__(self):
        return self.Pro_Name