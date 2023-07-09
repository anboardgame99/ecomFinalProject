# Generated by Django 4.2.2 on 2023-07-09 09:23

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_product_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='', primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]