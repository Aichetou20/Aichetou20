from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Product, ProductType, Wilaya, Moughataa, Commune, PointOfSale, CartProducts, Cart, ProductPrice


# ========================
# Vue pour la page d'accueil
# ========================
def home(request):
    return render(request, 'home.html')


# ========================
# Vues pour les Produits
# ========================
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

# ============================
# Vues pour les Types de Produits
# ============================
class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'producttype_list.html'
    context_object_name = 'producttypes'

class ProductTypeCreateView(CreateView):
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = 'producttype_form.html'
    success_url = reverse_lazy('producttype-list')

class ProductTypeUpdateView(UpdateView):
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = 'producttype_form.html'
    success_url = reverse_lazy('producttype-list')

class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = 'producttype_confirm_delete.html'
    success_url = reverse_lazy('producttype-list')

# =====================
# Vues pour les Wilayas
# =====================
class WilayaListView(ListView):
    model = Wilaya
    template_name = 'wilaya_list.html'
    context_object_name = 'wilayas'

class WilayaCreateView(CreateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = 'wilaya_form.html'
    success_url = reverse_lazy('wilaya-list')

class WilayaUpdateView(UpdateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = 'wilaya_form.html'
    success_url = reverse_lazy('wilaya-list')

class WilayaDeleteView(DeleteView):
    model = Wilaya
    template_name = 'wilaya_confirm_delete.html'
    success_url = reverse_lazy('wilaya-list')

# ========================
# Vues pour les Moughataas
# ========================
class MoughataaListView(ListView):
    model = Moughataa
    template_name = 'moughataa_list.html'
    context_object_name = 'moughataas'

class MoughataaCreateView(CreateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = 'moughataa_form.html'
    success_url = reverse_lazy('moughataa-list')

class MoughataaUpdateView(UpdateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = 'moughataa_form.html'
    success_url = reverse_lazy('moughataa-list')

class MoughataaDeleteView(DeleteView):
    model = Moughataa
    template_name = 'moughataa_confirm_delete.html'
    success_url = reverse_lazy('moughataa-list')

# =====================
# Vues pour les Communes
# =====================
class CommuneListView(ListView):
    model = Commune
    template_name = 'commune_list.html'
    context_object_name = 'communes'

class CommuneCreateView(CreateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = 'commune_form.html'
    success_url = reverse_lazy('commune-list')

class CommuneUpdateView(UpdateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = 'commune_form.html'
    success_url = reverse_lazy('commune-list')

class CommuneDeleteView(DeleteView):
    model = Commune
    template_name = 'commune_confirm_delete.html'
    success_url = reverse_lazy('commune-list')

# ============================
# Vues pour les Points de Vente
# ============================
class PointOfSaleListView(ListView):
    model = PointOfSale
    template_name = 'pointofsale_list.html'
    context_object_name = 'pointofsales'

class PointOfSaleCreateView(CreateView):
    model = PointOfSale
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = 'pointofsale_form.html'
    success_url = reverse_lazy('pointofsale-list')

class PointOfSaleUpdateView(UpdateView):
    model = PointOfSale
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = 'pointofsale_form.html'
    success_url = reverse_lazy('pointofsale-list')

class PointOfSaleDeleteView(DeleteView):
    model = PointOfSale
    template_name = 'pointofsale_confirm_delete.html'
    success_url = reverse_lazy('pointofsale-list')

# =====================
# Vues pour CartProducts
# =====================
class CartProductListView(ListView):
    model = CartProducts
    template_name = 'cartproduct_list.html'
    context_object_name = 'cartproducts'

class CartProductCreateView(CreateView):
    model = CartProducts
    fields = ['id', 'product', 'cart', 'weight', 'date_from', 'date_to']  # Suppression de cart_product
    template_name = 'cartproduct_form.html'
    success_url = reverse_lazy('cartproduct-list')

class CartProductUpdateView(UpdateView):
    model = CartProducts
    fields = ['id', 'product', 'cart', 'weight', 'date_from', 'date_to']  # Suppression de cart_product
    template_name = 'cartproduct_form.html'
    success_url = reverse_lazy('cartproduct-list')

class CartProductDeleteView(DeleteView):
    model = CartProducts
    template_name = 'cartproduct_confirm_delete.html'
    success_url = reverse_lazy('cartproduct-list')




class ProductPriceListView(ListView):
    model = ProductPrice
    template_name = 'productprice_list.html'
    context_object_name = 'productprices'

class ProductPriceCreateView(CreateView):
    model = ProductPrice
    fields = ['value', 'date_from', 'date_to', 'product', 'point_of_sale']
    template_name = 'productprice_form.html'
    success_url = reverse_lazy('productprice-list')

class ProductPriceUpdateView(UpdateView):
    model = ProductPrice
    fields = ['value', 'date_from', 'date_to', 'product', 'point_of_sale']
    template_name = 'productprice_form.html'
    success_url = reverse_lazy('productprice-list')

class ProductPriceDeleteView(DeleteView):
    model = ProductPrice
    template_name = 'productprice_confirm_delete.html'
    success_url = reverse_lazy('productprice-list')


class CartListView(ListView):
    model = Cart
    template_name = 'cart_list.html'
    context_object_name = 'carts'

class CartCreateView(CreateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = 'cart_form.html'
    success_url = reverse_lazy('cart-list')

class CartUpdateView(UpdateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = 'cart_form.html'
    success_url = reverse_lazy('cart-list')

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart_confirm_delete.html'
    success_url = reverse_lazy('cart-list')


