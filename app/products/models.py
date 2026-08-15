from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Material (models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Diety (models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=False, blank=False)
    material = models.ForeignKey(Material, related_name='products', on_delete=models.SET_NULL, null=False, blank=False)
    diety = models.ForeignKey(Diety, related_name='products', on_delete=models.SET_NULL, null=False, blank=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=False, null=False)
    uid = models.CharField(max_length=255, unique=True, blank=False, null=False) #need to autogenrate by signals
    short_description = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    min_weight = models.CharField(max_length=100, blank=True, null=True)
    max_weight = models.CharField(max_length=100, blank=True, null=True) 
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='in_stock') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1024, blank=True, null=True) # Used if storing direct R2 URL
    object_key = models.CharField(max_length=500, blank=True, null=True) # Used if storing R2 object key
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    display_order = models.IntegerField(default=0)
    cover_photo = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.name}"