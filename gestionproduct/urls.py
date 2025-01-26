from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductTypeListView ,ProductTypeCreateView ,ProductTypeUpdateView ,ProductTypeDeleteView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),  # Liste des produits
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),





    path('producttypes/', ProductTypeListView.as_view(), name='producttype-list'),  # Liste des types de produits
    path('producttypes/create/', ProductTypeCreateView.as_view(), name='producttype-create'),  # Créer un type de produit
    path('producttypes/<int:pk>/update/', ProductTypeUpdateView.as_view(), name='producttype-update'),  # Modifier un type de produit
    path('producttypes/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='producttype-delete'),  # Supprimer un type de produit
]