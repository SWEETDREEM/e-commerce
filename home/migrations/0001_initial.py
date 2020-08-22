# Generated by Django 3.1 on 2020-08-20 11:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('facebook', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('telegram', models.CharField(max_length=255)),
                ('aboutus', ckeditor.fields.RichTextField()),
                ('contacts', ckeditor.fields.RichTextField()),
                ('status', models.CharField(choices=[('true', 'Msvjud'), ('False', 'Mavjud eams')], max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
