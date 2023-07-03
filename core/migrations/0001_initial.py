# Generated by Django 4.2.2 on 2023-06-22 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cart_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_description', models.TextField()),
                ('order_location', models.CharField(max_length=100)),
                ('order_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Name')),
                ('product_description', models.TextField(verbose_name='Description')),
                ('product_image_url', models.URLField(null=True, verbose_name='Image URL')),
                ('product_quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('promotion_name', models.CharField(max_length=100)),
                ('promotion_quantity', models.PositiveIntegerField()),
                ('promotion_start_date', models.DateField()),
                ('promotion_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SupportCase',
            fields=[
                ('support_case_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]