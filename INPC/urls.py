from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestionproduct.urls')),
    path('accounts/', include('accounts.urls')),  # Inclure les URL de gestionproduct
]
