from django.urls import path
from .views import (
    home,
    # Product Views
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    # ProductType Views
    ProductTypeListView, ProductTypeCreateView, ProductTypeUpdateView, ProductTypeDeleteView,
    # Cart Views
    CartListView, CartCreateView, CartUpdateView, CartDeleteView,
    # ProductPrice Views
    ProductPriceListView ,ProductPriceCreateView, ProductPriceDeleteView, ProductPriceUpdateView,
    # Wilaya Views
    WilayaListView, WilayaCreateView, WilayaUpdateView, WilayaDeleteView,
    # Moughataa Views
    MoughataaListView, MoughataaCreateView, MoughataaUpdateView, MoughataaDeleteView,
    # Commune Views
    CommuneListView, CommuneCreateView, CommuneUpdateView, CommuneDeleteView,
    # PointOfSale Views
    PointOfSaleListView, PointOfSaleCreateView, PointOfSaleUpdateView, PointOfSaleDeleteView,
    #
    CartProductListView, CartProductCreateView,CartProductUpdateView,CartProductDeleteView
)

urlpatterns = [
    # Home Page
    path('',home, name='home'),

    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # ProductType URLs
    path('producttypes/', ProductTypeListView.as_view(), name='producttype-list'),
    path('producttypes/create/', ProductTypeCreateView.as_view(), name='producttype-create'),
    path('producttypes/<int:pk>/update/', ProductTypeUpdateView.as_view(), name='producttype-update'),
    path('producttypes/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='producttype-delete'),

    # Cart URLs
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/create/', CartCreateView.as_view(), name='cart-create'),
    path('carts/<int:pk>/update/', CartUpdateView.as_view(), name='cart-update'),
    path('carts/<int:pk>/delete/', CartDeleteView.as_view(), name='cart-delete'),

    # ProductPrice URLs
    path('productprices/', ProductPriceListView.as_view(), name='productprice-list'),
    path('productprices/create/', ProductPriceCreateView.as_view(), name='productprice-create'),
    path('productprices/<int:pk>/update/', ProductPriceUpdateView.as_view(), name='productprice-update'),
    path('productprices/<int:pk>/delete/', ProductPriceDeleteView.as_view(), name='productprice-delete'),

    # CartProducts URLs
    path('cartproducts/', CartProductListView.as_view(), name='cartproduct-list'),
    path('cartproducts/create/', CartProductCreateView.as_view(), name='cartproduct-create'),
    path('cartproducts/<str:pk>/update/', CartProductUpdateView.as_view(), name='cartproduct-update'),
    path('cartproducts/<str:pk>/delete/', CartProductDeleteView.as_view(), name='cartproduct-delete'),

    # Wilaya URLs
    path('wilayas/', WilayaListView.as_view(), name='wilaya-list'),
    path('wilayas/create/', WilayaCreateView.as_view(), name='wilaya-create'),
    path('wilayas/<int:pk>/update/', WilayaUpdateView.as_view(), name='wilaya-update'),
    path('wilayas/<int:pk>/delete/', WilayaDeleteView.as_view(), name='wilaya-delete'),

    # Moughataa URLs
    path('moughataas/', MoughataaListView.as_view(), name='moughataa-list'),
    path('moughataas/create/', MoughataaCreateView.as_view(), name='moughataa-create'),
    path('moughataas/<int:pk>/update/', MoughataaUpdateView.as_view(), name='moughataa-update'),
    path('moughataas/<int:pk>/delete/', MoughataaDeleteView.as_view(), name='moughataa-delete'),

    # Commune URLs
    path('communes/', CommuneListView.as_view(), name='commune-list'),
    path('communes/create/', CommuneCreateView.as_view(), name='commune-create'),
    path('communes/<int:pk>/update/', CommuneUpdateView.as_view(), name='commune-update'),
    path('communes/<int:pk>/delete/', CommuneDeleteView.as_view(), name='commune-delete'),

    # PointOfSale URLs
    path('pointofsales/', PointOfSaleListView.as_view(), name='pointofsale-list'),
    path('pointofsales/create/', PointOfSaleCreateView.as_view(), name='pointofsale-create'),
    path('pointofsales/<int:pk>/update/', PointOfSaleUpdateView.as_view(), name='pointofsale-update'),
    path('pointofsales/<int:pk>/delete/', PointOfSaleDeleteView.as_view(), name='pointofsale-delete'),
]
