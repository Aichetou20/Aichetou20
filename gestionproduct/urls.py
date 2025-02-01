from django.urls import path
from .views import calculate_inpc
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('inpc/<int:year>/<int:month>/', calculate_inpc, name='calculate_inpc'),
    

    # Product URLs
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
   

    # ProductType URLs
    path('producttypes/', views.ProductTypeListView.as_view(), name='producttype-list'),
    path('producttypes/create/', views.ProductTypeCreateView.as_view(), name='producttype-create'),
    path('producttypes/<int:pk>/update/', views.ProductTypeUpdateView.as_view(), name='producttype-update'),
    path('producttypes/<int:pk>/delete/', views.ProductTypeDeleteView.as_view(), name='producttype-delete'),
    path('export-producttypes/', views.export_product_types_to_excel, name='export_producttypes'),
    path('import-producttypes/', views.import_product_types_from_excel, name='import_producttypes'),

    # Cart URLs
    path('carts/', views.CartListView.as_view(), name='cart-list'),
    path('carts/create/', views.CartCreateView.as_view(), name='cart-create'),
    path('carts/<int:pk>/update/', views.CartUpdateView.as_view(), name='cart-update'),
    path('carts/<int:pk>/delete/', views.CartDeleteView.as_view(), name='cart-delete'),
    path('export-carts/', views.export_carts_to_excel, name='export_carts'),
    path('import-carts/', views.import_carts_from_excel, name='import_carts'),

    # ProductPrice URLs
    path('productprices/', views.ProductPriceListView.as_view(), name='productprice-list'),
    path('productprices/create/', views.ProductPriceCreateView.as_view(), name='productprice-create'),
    path('productprices/<int:pk>/update/', views.ProductPriceUpdateView.as_view(), name='productprice-update'),
    path('productprices/<int:pk>/delete/', views.ProductPriceDeleteView.as_view(), name='productprice-delete'),
    path('export-productprices/', views.export_product_prices_to_excel, name='export_productprices'),
    path('import-productprices/', views.import_product_prices_from_excel, name='import_productprices'),

    # CartProducts URLs
    path('cartproducts/', views.CartProductListView.as_view(), name='cartproduct-list'),
    path('cartproducts/create/', views.CartProductCreateView.as_view(), name='cartproduct-create'),
    path('cartproducts/<str:pk>/update/', views.CartProductUpdateView.as_view(), name='cartproduct-update'),
    path('cartproducts/<str:pk>/delete/', views.CartProductDeleteView.as_view(), name='cartproduct-delete'),
    path('export-cartproducts/', views.export_cartproducts_to_excel, name='export_cartproducts'),
    path('import-cartproducts/', views.import_cartproducts_from_excel, name='import_cartproducts'),


    # Wilaya URLs
    path('wilayas/', views.WilayaListView.as_view(), name='wilaya-list'),
    path('wilayas/create/', views.WilayaCreateView.as_view(), name='wilaya-create'),
    path('wilayas/<int:pk>/update/', views.WilayaUpdateView.as_view(), name='wilaya-update'),
    path('wilayas/<int:pk>/delete/', views.WilayaDeleteView.as_view(), name='wilaya-delete'),
    path('export-wilayas/', views.export_wilayas_to_excel, name='export_wilayas'),
    path('import-wilayas/', views.import_wilayas_from_excel, name='import_wilayas'),


    # Moughataa URLs
    path('moughataas/', views.MoughataaListView.as_view(), name='moughataa-list'),
    path('moughataas/create/', views.MoughataaCreateView.as_view(), name='moughataa-create'),
    path('moughataas/<int:pk>/update/', views.MoughataaUpdateView.as_view(), name='moughataa-update'),
    path('moughataas/<int:pk>/delete/', views.MoughataaDeleteView.as_view(), name='moughataa-delete'),
    path('export-moughataas/', views.export_moughataas_to_excel, name='export_moughataas'),
    path('import-moughataas/', views.import_moughataas_from_excel, name='import_moughataas'),


    # Commune URLs
    path('communes/', views.CommuneListView.as_view(), name='commune-list'),
    path('communes/create/', views.CommuneCreateView.as_view(), name='commune-create'),
    path('communes/<int:pk>/update/', views.CommuneUpdateView.as_view(), name='commune-update'),
    path('communes/<int:pk>/delete/', views.CommuneDeleteView.as_view(), name='commune-delete'),
    path('export-communes/', views.export_communes_to_excel, name='export_communes'),
    path('import-communes/', views.import_communes_from_excel, name='import_communes'),



    # PointOfSale URLs
    path('pointofsales/', views.PointOfSaleListView.as_view(), name='pointofsale-list'),
    path('pointofsales/create/', views.PointOfSaleCreateView.as_view(), name='pointofsale-create'),
    path('pointofsales/<int:pk>/update/', views.PointOfSaleUpdateView.as_view(), name='pointofsale-update'),
    path('pointofsales/<int:pk>/delete/', views.PointOfSaleDeleteView.as_view(), name='pointofsale-delete'),
    # ✅ Ajouter l'URL d'importation
    path('pointofsales/import/', views.import_pointofsales_from_excel, name='import_pointofsales'),

    # ✅ Ajouter une URL pour l'exportation
    path('pointofsales/export/', views.export_pointofsales_to_excel, name='export_pointofsales'),
    path('export-products/', views.export_products_to_excel, name='export_products'),
    path('import-products/', views.import_products_from_excel, name='import_products')

]
