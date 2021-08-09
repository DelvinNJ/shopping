from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='media/category',blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)

class ProductModel(models.Model):
    def __str__(self):
        return self.name
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/product',blank=True)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)


class CartListModel(models.Model):
    cart_id = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)


class CartItemModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    cartList = models.ForeignKey(CartListModel,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    def total(self):
        return self.product.price * self.quantity






