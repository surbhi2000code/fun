from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=505,default="")
    price = models.IntegerField(default="")
    image = models.ImageField(upload_to='lol/images',default="")
    desc = models.CharField(max_length=700)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    mobile = models.CharField(max_length=505,default="")
    desc = models.CharField(max_length=700)

    #image = models.ImageField(upload_to='lol/images',default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    mobile = models.CharField(max_length=505, default="")
    address = models.CharField(max_length=700)
    state = models.CharField(max_length=700)
    city = models.CharField(max_length=700)
    zip_code = models.CharField(max_length=700)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=7000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."