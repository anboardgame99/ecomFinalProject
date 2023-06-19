from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

STATUS_CHOICE = (
    ('process', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)

RATING = (
    ("1", "★☆☆☆☆"),
    ("2", "★★☆☆☆"),
    ("3", "★★★☆☆"),
    ("4", "★★★★☆"),
    ("5", "★★★★★"),
)

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="User")

    product_id = models.AutoField(primary_key=True, verbose_name="ID")
    product_name = models.CharField(max_length=100, verbose_name="Name")
    product_description = models.TextField(verbose_name="Description")
    product_image = models.ImageField(upload_to=user_directory_path, default="product.jpg", verbose_name="Image")
    # product_image_url = models.URLField(null=True, verbose_name="Image URL")
    product_quantity = models.PositiveIntegerField(verbose_name="Quantity")
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")


    def __str__(self):
        return self.product_name

    def image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.product_image.url))

class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_description = models.TextField()
    order_location = models.CharField(max_length=100)
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return self.order_id

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', null=True, blank=True, on_delete=models.SET_NULL)
    cart_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cart_id



class SupportCase(models.Model):
    support_case_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', null=True, blank=True, on_delete=models.SET_NULL)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    warranty_id = models.ForeignKey('coverage.Warranty', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.support_case_id

class Promotion(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    promotion_name = models.CharField(max_length=100)
    promotion_quantity = models.PositiveIntegerField()
    promotion_start_date = models.DateField()
    promotion_end_date = models.DateField()

    def __str__(self):
        return self.promotion_id

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', null=True, blank=True, on_delete=models.SET_NULL)
    promotion_id = models.ForeignKey('Promotion', null=True, blank=True, on_delete=models.SET_NULL)
    cart_id = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_id

