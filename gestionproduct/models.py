from django.db import models

class INPC(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    inpc_value = models.FloatField()

    class Meta:
        unique_together = ('year', 'month')  # Évite les doublons pour un même mois et année

    def __str__(self):
        return f"INPC {self.year}-{self.month}: {self.inpc_value}"

class ProductType(models.Model):
    code = models.CharField(max_length=45, unique=True)
    label = models.CharField(max_length=45)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Product(models.Model):
    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    unit_measure = models.CharField(max_length=45)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wilaya(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Moughataa(models.Model):
    code = models.CharField(max_length=45, unique=True)
    label = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.label} ({self.wilaya.name})"

class Commune(models.Model):
    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=100)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.moughataa.label})"

class PointOfSale(models.Model):
    code = models.CharField(max_length=45, unique=True)
    type = models.CharField(max_length=45)
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.commune.name}"

class ProductPrice(models.Model):
    value = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    point_of_sale = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.value} ({self.point_of_sale.code})"

class CartProducts(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return f"{self.product.name} in {self.cart.name} (Weight: {self.weight})"
