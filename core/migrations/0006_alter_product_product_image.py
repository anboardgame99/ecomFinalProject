# Generated by Django 4.2.2 on 2023-06-27 21:36

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='product.jpg', upload_to=core.models.user_directory_path, verbose_name='Image'),
        ),
    ]
