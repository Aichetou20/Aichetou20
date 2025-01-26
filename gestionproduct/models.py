from django.db import models

class ProductType(models.Model):
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.label
    
class Product(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    unit_measure = models.CharField(max_length=45)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.name
    

class Wilaya(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=252)

    def __str__(self):
        return self.name
    


class ProductPrice(models.Model):
    value = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    point_of_sale = models.ForeignKey('PointOfSale', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.value}"
    

class PartProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Cart, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField()
    id = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return f"{self.product.name} - {self.cart_product.name}"
    

class Moughataa(models.Model):
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
    

class Commune(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class PointOfSale(models.Model):
    code = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
    

