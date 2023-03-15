from django.db import models

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='shop/images',default="")


    def __str__(self):
        return self.name


class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class food(models.Model):
    class foodchoices(models.TextChoices):
        snacks='s'
        main_course='m'
        beverages='b'
        drinks='d'
    class Type(models.TextChoices):
        veg='veg'
        nonveg='non-veg'

    Name=models.TextField(default=0)
    Region=models.CharField(max_length=100)
    Cuisines=models.CharField(max_length=1,choices=foodchoices.choices)
    Ratings=models.PositiveIntegerField(default=0)
    Type=models.CharField(max_length=50,choices=Type.choices)