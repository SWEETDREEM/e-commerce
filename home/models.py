from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('true', 'Msvjud'),
        ('False', 'Mavjud eams')
    )
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = RichTextField()
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    fax = models.IntegerField()
    email = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    aboutus = RichTextField()
    contacts = RichTextField()
    status = models.CharField(max_length=15, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.title