from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class CustomizeRequest(models.Model):
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    approximate_height = models.CharField(max_length=100, blank=True, null=True)
    preferred_material = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    reference_image = models.URLField(max_length=1024, blank=True, null=True) # Could be R2 URL
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Customize Request from {self.city} - {self.status}"