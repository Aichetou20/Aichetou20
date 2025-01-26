from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Chemin corrigé

class ProductCreateView(CreateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure']
    template_name = 'product_form.html'  # Chemin corrigé
    success_url = '/products/'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure']
    template_name = 'product_form.html'  # Chemin corrigé
    success_url = '/products/'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'  # Chemin corrigé
    success_url = '/products/'


from django.urls import reverse_lazy
from .models import ProductType

# Vue pour lister les types de produits
class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'producttype_list.html'  # Template pour afficher la liste
    context_object_name = 'producttypes'  # Nom de la variable passée au template

# Vue pour créer un nouveau type de produit
class ProductTypeCreateView(CreateView):
    model = ProductType
    fields = ['code', 'label', 'description']  # Champs du formulaire
    template_name = 'producttype_form.html'  # Template pour le formulaire
    success_url = reverse_lazy('producttype-list')  # Redirection après création

# Vue pour modifier un type de produit existant
class ProductTypeUpdateView(UpdateView):
    model = ProductType
    fields = ['code', 'label', 'description']  # Champs du formulaire
    template_name = 'producttype_form.html'  # Template pour le formulaire
    success_url = reverse_lazy('producttype-list')  # Redirection après modification

# Vue pour supprimer un type de produit
class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = 'producttype_confirm_delete.html'  # Template de confirmation
    success_url = reverse_lazy('producttype-list')  # Redirection après suppression