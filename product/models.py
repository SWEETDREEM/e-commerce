from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS=(
        ('New', 'Yangi'),
        ('False', 'Mavjud emas'),
    )
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.title


class Product(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('False', 'mavjudmas'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    detail = RichTextField()
    minamount = models.ImageField()
    amout = models.IntegerField()
    price = models.FloatField


    def __str__(self):
         self.title


    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/products/images/')

    def __str__(self):
        self.title