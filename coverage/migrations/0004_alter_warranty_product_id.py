# Generated by Django 4.2.2 on 2023-06-28 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_supportcase_warranty_id_delete_warranty'),
        ('coverage', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='product_id',
            field=models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
