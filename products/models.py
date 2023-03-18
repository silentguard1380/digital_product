from django.db import models

# Create your models here.



class Category(models.Model):

    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    avatar = models.ImageField(blank=True,upload_to='categories')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    avatar = models.ImageField(blank=True, upload_to='categories')
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category',blank=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class File(models.Model):

    product = models.ForeignKey('Product',on_delete=models.CASCADE,verbose_name='product')
    title = models.CharField(max_length=50)

    file = models.FileField(upload_to='files/%Y/%m/%d/')

    is_enable = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'