from django.db import models

class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_deleted=False)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
    
    # def soft_deleted(self):
    #     return self.get_queryset().filter(is_deleted=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.name
