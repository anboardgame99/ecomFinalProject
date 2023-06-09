# Generated by Django 4.2.2 on 2023-06-28 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0011_remove_warranty_product_id'),
        ('coverage', '0002_delete_warranty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('warranty_id', models.AutoField(primary_key=True, serialize=False)),
                ('warranty_description', models.TextField()),
                ('warranty_status', models.CharField(max_length=50)),
                ('warranty_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
