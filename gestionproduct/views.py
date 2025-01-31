from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Product, ProductType, Wilaya, Moughataa, Commune, PointOfSale, CartProducts, Cart, ProductPrice
import json


from django.http import HttpResponse

from django.contrib import messages

import pandas as pd



# ========================
# Vue pour la page d'accueil
# ========================
from django.shortcuts import render
from .models import INPC

# views.py
import json
from django.shortcuts import render
from .models import INPC

def home(request):
    # Récupérer les 4 derniers INPC triés par date décroissante
    last_4_inpc = INPC.objects.order_by('-year', '-month')[:4]
    
    # Convertir les données en JSON
    inpc_data = list(last_4_inpc.values('year', 'month', 'inpc_value'))
    inpc_data_json = json.dumps(inpc_data)
    
    # Passer les données au template
    context = {
        'inpc_data': last_4_inpc,          # Pour le tableau
        'inpc_data_json': inpc_data_json   # Pour les graphiques
    }
    return render(request, 'home.html', context)


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



import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import ProductType
import openpyxl

def export_product_types_to_excel(request):
    """Exporter la liste des types de produits sous format Excel"""
    product_types = ProductType.objects.all().values('code', 'label', 'description')

    df = pd.DataFrame(product_types)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=product_types.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='ProductTypes')

    return response


def import_product_types_from_excel(request):
    """Importer des types de produits depuis un fichier Excel"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')

            for _, row in df.iterrows():
                ProductType.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'label': row['label'],
                        'description': row['description'],
                    }
                )

            messages.success(request, "Importation des types de produits réussie !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return HttpResponseRedirect(reverse('producttype-list'))  # Redirection vers la liste des types de produits

    return HttpResponseRedirect(reverse('producttype-list'))  # Si pas de fichier, retour à la liste des types de produits


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



import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Wilaya
import openpyxl

def export_wilayas_to_excel(request):
    """Exporter la liste des wilayas sous format Excel"""
    wilayas = Wilaya.objects.all().values('code', 'name')

    df = pd.DataFrame(wilayas)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=wilayas.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Wilayas')

    return response


def import_wilayas_from_excel(request):
    """Importer des wilayas depuis un fichier Excel"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')

            for _, row in df.iterrows():
                Wilaya.objects.update_or_create(
                    code=row['code'],
                    defaults={'name': row['name']}
                )

            messages.success(request, "Importation des wilayas réussie !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return HttpResponseRedirect(reverse('wilaya-list'))  # Redirection vers la liste des wilayas

    return HttpResponseRedirect(reverse('wilaya-list'))  # Si pas de fichier, retour à la liste des wilayas


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


import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Moughataa, Wilaya
import openpyxl

def export_moughataas_to_excel(request):
    """Exporter la liste des Moughataas sous format Excel"""
    moughataas = Moughataa.objects.all().values('code', 'label', 'wilaya__name')

    df = pd.DataFrame(moughataas)
    df.rename(columns={'wilaya__name': 'wilaya'}, inplace=True)  # Renommer la colonne pour clarté

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=moughataas.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Moughataas')

    return response


def import_moughataas_from_excel(request):
    """Importer des Moughataas depuis un fichier Excel"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')

            for _, row in df.iterrows():
                try:
                    wilaya = Wilaya.objects.get(name=row['wilaya'])  # Vérifier si la wilaya existe
                    Moughataa.objects.update_or_create(
                        code=row['code'],
                        defaults={'label': row['label'], 'wilaya': wilaya}
                    )
                except Wilaya.DoesNotExist:
                    messages.error(request, f"Wilaya {row['wilaya']} non trouvée.")

            messages.success(request, "Importation des Moughataas réussie !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return HttpResponseRedirect(reverse('moughataa-list'))  # Redirection vers la liste des Moughataas

    return HttpResponseRedirect(reverse('moughataa-list'))  # Si pas de fichier, retour à la liste des Moughataas


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


import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Commune, Moughataa
import openpyxl

def export_communes_to_excel(request):
    """Exporter la liste des Communes sous format Excel"""
    communes = Commune.objects.all().values('code', 'name', 'moughataa__label')

    df = pd.DataFrame(communes)
    df.rename(columns={'moughataa__label': 'moughataa'}, inplace=True)  # Renommer la colonne pour clarté

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=communes.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Communes')

    return response


def import_communes_from_excel(request):
    """Importer des Communes depuis un fichier Excel"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')

            for _, row in df.iterrows():
                try:
                    moughataa = Moughataa.objects.get(label=row['moughataa'])  # Vérifier si la Moughataa existe
                    Commune.objects.update_or_create(
                        code=row['code'],
                        defaults={'name': row['name'], 'moughataa': moughataa}
                    )
                except Moughataa.DoesNotExist:
                    messages.error(request, f"Moughataa {row['moughataa']} non trouvée.")

            messages.success(request, "Importation des Communes réussie !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return HttpResponseRedirect(reverse('commune-list'))  # Redirection vers la liste des Communes

    return HttpResponseRedirect(reverse('commune-list'))  # Si pas de fichier, retour à la liste des Communes


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


import pandas as pd
from django.http import HttpResponse
from .models import CartProducts

def export_cartproducts_to_excel(request):
    """Exporter la liste des produits dans les paniers sous format Excel"""
    cart_products = CartProducts.objects.all().values('cart__id', 'product__code', 'weight')

    df = pd.DataFrame(cart_products)
    df.rename(columns={'cart__id': 'cart_id', 'product__code': 'product_code', 'weight': 'weight'}, inplace=True)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=cart_products.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='CartProducts')

    return response



def import_cartproducts_from_excel(request):
    """Importer des produits dans les paniers depuis un fichier Excel"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')

            for _, row in df.iterrows():
                try:
                    cart = Cart.objects.get(id=row['cart_id'])  # Vérifie si le panier existe
                    product = Product.objects.get(code=row['product_code'])  # Vérifie si le produit existe
                    CartProducts.objects.update_or_create(
                        cart=cart,
                        product=product,
                        defaults={'quantity': row['quantity']}  # Ajout ou mise à jour de la quantité
                    )
                except Cart.DoesNotExist:
                    messages.error(request, f"Panier avec ID {row['cart_id']} non trouvé.")
                except Product.DoesNotExist:
                    messages.error(request, f"Produit avec code {row['product_code']} non trouvé.")

            messages.success(request, "Importation des produits dans les paniers réussie !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return HttpResponseRedirect(reverse('cartproducts-list'))  # Redirection vers la liste des produits dans les paniers

    return HttpResponseRedirect(reverse('cartproducts-list'))  # Si pas de fichier, retour à la liste des produits dans les paniers






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



    import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import ProductPrice, Product
import openpyxl

def export_product_prices_to_excel(request):
    """Exporter la liste des prix des produits sous format Excel"""
    product_prices = ProductPrice.objects.all().values('product__code', 'value', 'date_from', 'date_to')

    df = pd.DataFrame(product_prices)
    df.rename(columns={'product__code': 'product_code', 'value': 'price', 'date_from': 'start_date', 'date_to': 'end_date'}, inplace=True)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=product_prices.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='ProductPrices')

    return response



def import_product_prices_from_excel(request):
    """Importer des prix de produits depuis un fichier Excel"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')

            for _, row in df.iterrows():
                try:
                    product = Product.objects.get(code=row['product_code'])  # Vérifier si le produit existe
                    ProductPrice.objects.update_or_create(
                        product=product,
                        date=row['date'],
                        defaults={'price': row['price']}
                    )
                except Product.DoesNotExist:
                    messages.error(request, f"Produit avec code {row['product_code']} non trouvé.")

            messages.success(request, "Importation des prix des produits réussie !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return HttpResponseRedirect(reverse('productprice-list'))  # Redirection vers la liste des prix

    return HttpResponseRedirect(reverse('productprice-list'))  # Si pas de fichier, retour à la liste des prix



def product_prices_list(request):
    product_prices = ProductPrice.objects.all().values('id', 'product__code', 'product__name', 'value', 'date_from', 'date_to')
    return render(request, 'product_prices_list.html', {'product_prices': product_prices})
print(list(ProductPrice.objects.all().values()))



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


import pandas as pd
from django.http import HttpResponse
from .models import Cart

def export_carts_to_excel(request):
    """Exporter la liste des paniers sous format Excel"""
    carts = Cart.objects.all().values('id', 'code', 'name', 'description')

    df = pd.DataFrame(carts)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=carts.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Carts')

    return response



def import_carts_from_excel(request):
    """Importer des paniers depuis un fichier Excel"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')

            for _, row in df.iterrows():
                Cart.objects.update_or_create(
                    id=row['id'],
                    defaults={
                        'user': row['user'],
                        'created_at': row['created_at'],
                    }
                )

            messages.success(request, "Importation des paniers réussie !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return HttpResponseRedirect(reverse('cart-list'))  # Redirection vers la liste des paniers

    return HttpResponseRedirect(reverse('cart-list'))  # Si pas de fichier, retour à la liste des paniers




from .models import Product, ProductType
import openpyxl

def export_products_to_excel(request):
    """Exporter la liste des produits sous format Excel"""
    products = Product.objects.all().values('code', 'name', 'description', 'unit_measure', 'product_type__label')
    
    df = pd.DataFrame(products)
    df.rename(columns={'product_type__label': 'product_type'}, inplace=True)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'
    
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Products')
    
    return response
from django.http import HttpResponseRedirect
from django.urls import reverse

def import_products_from_excel(request):
    """Importer des produits depuis un fichier Excel depuis la liste des produits"""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        
        try:
            df = pd.read_excel(excel_file, engine='openpyxl')
            
            for _, row in df.iterrows():
                product_type, created = ProductType.objects.get_or_create(label=row['product_type'])
                Product.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'name': row['name'],
                        'description': row['description'],
                        'unit_measure': row['unit_measure'],
                        'product_type': product_type
                    }
                )
            
            messages.success(request, "Importation réussie!")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")
        
        return HttpResponseRedirect(reverse('product-list'))  # Redirection vers la liste des produits

    return HttpResponseRedirect(reverse('product-list'))  # Si pas de fichier, retour à la liste des produits


#calcule INPC

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg
from .models import ProductPrice

def calculate_inpc(request, year, month):
    """
    Calcule l'Indice National des Prix à la Consommation (INPC) pour un mois donné.
    """
    # Filtrer les prix qui couvrent la période demandée
    prices = ProductPrice.objects.filter(date_from__year=year, date_from__month=month)
    
    if not prices.exists():
        return JsonResponse({"error": "Pas assez de données pour calculer l'INPC."}, status=400)

    # Calcul de l'INPC (exemple : moyenne des prix des produits)
    average_price = prices.aggregate(Avg('value'))['value__avg']

    return JsonResponse({
        "year": year,
        "month": month,
        "inpc_value": average_price
    })




# views.py

from django.shortcuts import render
from .models import INPC, ProductType, Product, ProductPrice
from django.db.models import Count, Avg
import json

def dashboard_view(request):
    # Données pour le Line Chart : Évolution de l'INPC sur les derniers mois
    last_12_inpc = INPC.objects.order_by('-year', '-month')[:12]
    inpc_labels = [f"{item.month}/{item.year}" for item in last_12_inpc]
    inpc_values = [item.inpc_value for item in last_12_inpc]

    # Données pour le Pie Chart : Répartition des types de produits
    product_types = ProductType.objects.annotate(total_products=Count('product'))
    pie_labels = [pt.label for pt in product_types]
    pie_data = [pt.total_products for pt in product_types]

    # Données pour le Bar Chart : Nombre de produits par type
    bar_labels = [pt.label for pt in product_types]
    bar_data = [pt.total_products for pt in product_types]

    # **Nouvelles Données pour l'Évolution des Prix**
    # Calculer l'évolution moyenne des prix par mois
    price_evolution = ProductPrice.objects.values('date_from__year', 'date_from__month') \
        .annotate(avg_price=Avg('value')) \
        .order_by('date_from__year', 'date_from__month')

    price_labels = [f"{item['date_from__month']}/{item['date_from__year']}" for item in price_evolution]
    price_values = [item['avg_price'] for item in price_evolution]

    context = {
        'inpc_labels': json.dumps(inpc_labels[::-1]),  # Inversion pour chronologie
        'inpc_values': json.dumps(inpc_values[::-1]),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'price_labels': json.dumps(price_labels),
        'price_values': json.dumps(price_values),
    }

    return render(request, 'dashboard.html', context)



from django.db.models import Avg
import json
from django.shortcuts import render
from .models import ProductPrice

def dashboard_view(request):
    # Récupérer les prix moyens par mois
    price_evolution = ProductPrice.objects.values('date_from__year', 'date_from__month') \
        .annotate(avg_price=Avg('value')) \
        .order_by('date_from__year', 'date_from__month')

    price_labels = [f"{item['date_from__month']}/{item['date_from__year']}" for item in price_evolution]
    price_values = [item['avg_price'] for item in price_evolution]

    context = {
        'price_labels': json.dumps(price_labels),
        'price_values': json.dumps(price_values),
    }

    return render(request, 'dashboard.html', context)



from django.db.models import Count
from .models import ProductType, Product

def dashboard_view(request):
    # Nombre de produits par type
    product_types = ProductType.objects.annotate(total_products=Count('product'))

    pie_labels = [pt.label for pt in product_types]
    pie_data = [pt.total_products for pt in product_types]

    context.update({
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
    })

    return render(request, 'dashboard.html', context)



from django.shortcuts import render
from django.db.models import Count, Avg
import json
from .models import ProductPrice, ProductType, PointOfSale, INPC

def dashboard_view(request):
    context = {}

    # 1️⃣ Évolution de l'INPC (Déjà ajouté)
    inpc_data = INPC.objects.order_by('year', 'month')
    inpc_labels = [f"{entry.month}/{entry.year}" for entry in inpc_data]
    inpc_values = [entry.inpc_value for entry in inpc_data]

    # 2️⃣ Évolution Moyenne des Prix des Produits par Mois
    price_evolution = ProductPrice.objects.values('date_from__year', 'date_from__month') \
        .annotate(avg_price=Avg('value')) \
        .order_by('date_from__year', 'date_from__month')

    price_labels = [f"{item['date_from__month']}/{item['date_from__year']}" for item in price_evolution]
    price_values = [item['avg_price'] for item in price_evolution]

    # 3️⃣ Répartition des Types de Produits (Pie Chart)
    product_types = ProductType.objects.annotate(total_products=Count('product'))
    pie_labels = [pt.label for pt in product_types]
    pie_data = [pt.total_products for pt in product_types]

    # 4️⃣ Nombre de Produits par Type (Bar Chart)
    bar_labels = pie_labels  # Même que Pie Chart
    bar_data = pie_data      # Même que Pie Chart

    # 5️⃣ Nombre de Produits par Point de Vente (Bar Chart - Déjà ajouté)
    points_of_sale = PointOfSale.objects.annotate(total_products=Count('productprice'))
    pos_labels = [pos.code for pos in points_of_sale]
    pos_data = [pos.total_products for pos in points_of_sale]

    # Ajouter les données au contexte
    context.update({
        'inpc_labels': json.dumps(inpc_labels),
        'inpc_values': json.dumps(inpc_values),
        'price_labels': json.dumps(price_labels),
        'price_values': json.dumps(price_values),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'pos_labels': json.dumps(pos_labels),
        'pos_data': json.dumps(pos_data),
    })

    return render(request, 'dashboard.html', context)



from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'gestionproduct/dashboard.html')
