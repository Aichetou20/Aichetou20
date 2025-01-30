from django.urls import path
from .views import calculate_inpc



from . import views  as viwes # Correction ici



urlpatterns = [
    # Home Page
    path('',viwes.home, name='home'),

    path('dashboard/', viwes.dashboard_view, name='dashboard'),


    path('inpc/<int:year>/<int:month>/', calculate_inpc, name='calculate_inpc'),
    

    # Product URLs
    path('products/', viwes.ProductListView.as_view(), name='product-list'),
    path('products/create/', viwes.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', viwes.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', viwes.ProductDeleteView.as_view(), name='product-delete'),
   

    # ProductType URLs
    path('producttypes/', viwes.ProductTypeListView.as_view(), name='producttype-list'),
    path('producttypes/create/', viwes.ProductTypeCreateView.as_view(), name='producttype-create'),
    path('producttypes/<int:pk>/update/', viwes.ProductTypeUpdateView.as_view(), name='producttype-update'),
    path('producttypes/<int:pk>/delete/', viwes.ProductTypeDeleteView.as_view(), name='producttype-delete'),
    path('export-producttypes/', viwes.export_product_types_to_excel, name='export_producttypes'),
    path('import-producttypes/', viwes.import_product_types_from_excel, name='import_producttypes'),

    # Cart URLs
    path('carts/', viwes.CartListView.as_view(), name='cart-list'),
    path('carts/create/', viwes.CartCreateView.as_view(), name='cart-create'),
    path('carts/<int:pk>/update/', viwes.CartUpdateView.as_view(), name='cart-update'),
    path('carts/<int:pk>/delete/', viwes.CartDeleteView.as_view(), name='cart-delete'),
    path('export-carts/', viwes.export_carts_to_excel, name='export_carts'),
    path('import-carts/', viwes.import_carts_from_excel, name='import_carts'),

    # ProductPrice URLs
    path('productprices/', viwes.ProductPriceListView.as_view(), name='productprice-list'),
    path('productprices/create/', viwes.ProductPriceCreateView.as_view(), name='productprice-create'),
    path('productprices/<int:pk>/update/', viwes.ProductPriceUpdateView.as_view(), name='productprice-update'),
    path('productprices/<int:pk>/delete/', viwes.ProductPriceDeleteView.as_view(), name='productprice-delete'),
    path('export-productprices/', viwes.export_product_prices_to_excel, name='export_productprices'),
    path('import-productprices/', viwes.import_product_prices_from_excel, name='import_productprices'),

    # CartProducts URLs
    path('cartproducts/', viwes.CartProductListView.as_view(), name='cartproduct-list'),
    path('cartproducts/create/', viwes.CartProductCreateView.as_view(), name='cartproduct-create'),
    path('cartproducts/<str:pk>/update/', viwes.CartProductUpdateView.as_view(), name='cartproduct-update'),
    path('cartproducts/<str:pk>/delete/', viwes.CartProductDeleteView.as_view(), name='cartproduct-delete'),
    path('export-cartproducts/', viwes.export_cartproducts_to_excel, name='export_cartproducts'),
    path('import-cartproducts/', viwes.import_cartproducts_from_excel, name='import_cartproducts'),


    # Wilaya URLs
    path('wilayas/', viwes.WilayaListView.as_view(), name='wilaya-list'),
    path('wilayas/create/', viwes.WilayaCreateView.as_view(), name='wilaya-create'),
    path('wilayas/<int:pk>/update/', viwes.WilayaUpdateView.as_view(), name='wilaya-update'),
    path('wilayas/<int:pk>/delete/', viwes.WilayaDeleteView.as_view(), name='wilaya-delete'),
    path('export-wilayas/', viwes.export_wilayas_to_excel, name='export_wilayas'),
    path('import-wilayas/', viwes.import_wilayas_from_excel, name='import_wilayas'),


    # Moughataa URLs
    path('moughataas/', viwes.MoughataaListView.as_view(), name='moughataa-list'),
    path('moughataas/create/', viwes.MoughataaCreateView.as_view(), name='moughataa-create'),
    path('moughataas/<int:pk>/update/', viwes.MoughataaUpdateView.as_view(), name='moughataa-update'),
    path('moughataas/<int:pk>/delete/', viwes.MoughataaDeleteView.as_view(), name='moughataa-delete'),
    path('export-moughataas/', viwes.export_moughataas_to_excel, name='export_moughataas'),
    path('import-moughataas/', viwes.import_moughataas_from_excel, name='import_moughataas'),


    # Commune URLs
    path('communes/', viwes.CommuneListView.as_view(), name='commune-list'),
    path('communes/create/', viwes.CommuneCreateView.as_view(), name='commune-create'),
    path('communes/<int:pk>/update/', viwes.CommuneUpdateView.as_view(), name='commune-update'),
    path('communes/<int:pk>/delete/', viwes.CommuneDeleteView.as_view(), name='commune-delete'),
    path('export-communes/', viwes.export_communes_to_excel, name='export_communes'),
    path('import-communes/', viwes.import_communes_from_excel, name='import_communes'),



    # PointOfSale URLs
    path('pointofsales/', viwes.PointOfSaleListView.as_view(), name='pointofsale-list'),
    path('pointofsales/create/', viwes.PointOfSaleCreateView.as_view(), name='pointofsale-create'),
    path('pointofsales/<int:pk>/update/', viwes.PointOfSaleUpdateView.as_view(), name='pointofsale-update'),
    path('pointofsales/<int:pk>/delete/', viwes.PointOfSaleDeleteView.as_view(), name='pointofsale-delete'),
    path('export-products/', viwes.export_products_to_excel, name='export_products'),
    path('import-products/', viwes.import_products_from_excel, name='import_products')

]
