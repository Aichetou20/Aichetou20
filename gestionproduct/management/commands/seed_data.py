from django.core.management.base import BaseCommand
from gestionproduct.models import (
    INPC, ProductType, Product, Cart, Wilaya, 
    Moughataa, Commune, PointOfSale, ProductPrice, CartProducts
)
import pandas as pd
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Seeds the database with data from Excel files'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete data in reverse order of dependencies
        CartProducts.objects.all().delete()
        ProductPrice.objects.all().delete()
        PointOfSale.objects.all().delete()
        Commune.objects.all().delete()
        Moughataa.objects.all().delete()
        Wilaya.objects.all().delete()
        Cart.objects.all().delete()
        Product.objects.all().delete()
        ProductType.objects.all().delete()
        INPC.objects.all().delete()

        dataset_path = os.path.join(settings.BASE_DIR, 'dataset')
        
        self.stdout.write('Loading data from Excel files...')

        # Load Wilayas
        df_wilayas = pd.read_excel(os.path.join(dataset_path, 'wilayas.xlsx'))
        created_wilayas = {}
        for _, row in df_wilayas.iterrows():
            wilaya = Wilaya.objects.create(
                code=str(row['code']),  # Convert to string since it's coming as int
                name=row['name']
            )
            created_wilayas[wilaya.name] = wilaya  # Use name as key since that's what moughataas.xlsx uses
        self.stdout.write(f'Created {len(created_wilayas)} wilayas')

        # Load Moughataas
        df_moughataas = pd.read_excel(os.path.join(dataset_path, 'moughataas.xlsx'))
        created_moughataas = {}
        for _, row in df_moughataas.iterrows():
            moughataa = Moughataa.objects.create(
                code=str(row['code']),  # Convert to string since it's coming as int
                label=row['label'],
                wilaya=created_wilayas[row['wilaya']]  # Use wilaya name to look up
            )
            created_moughataas[moughataa.label] = moughataa  # Use label as key since communes.xlsx uses it
        self.stdout.write(f'Created {len(created_moughataas)} moughataas')

        # Load Communes
        df_communes = pd.read_excel(os.path.join(dataset_path, 'communes.xlsx'))
        created_communes = {}
        for _, row in df_communes.iterrows():
            commune = Commune.objects.create(
                code=str(row['code']),
                name=row['name'],
                moughataa=created_moughataas[row['moughataa']]  # Use moughataa label to look up
            )
            created_communes[commune.code] = commune
        self.stdout.write(f'Created {len(created_communes)} communes')

        # Create PointOfSale for each commune
        created_points_of_sale = {}
        for commune_code, commune in created_communes.items():
            point_of_sale = PointOfSale.objects.create(
                code=f"POS_{commune_code}",
                type="Standard",  # Default type
                gps_lat=18.0735,  # Default latitude for Nouakchott
                gps_lon=-15.9582,  # Default longitude for Nouakchott
                commune=commune
            )
            created_points_of_sale[commune_code] = point_of_sale
        self.stdout.write(f'Created {len(created_points_of_sale)} points of sale')

        # Load Product Types
        df_product_types = pd.read_excel(os.path.join(dataset_path, 'product_types.xlsx'))
        created_types = {}
        for _, row in df_product_types.iterrows():
            product_type = ProductType.objects.create(
                code=str(row['code']),
                label=row['label'],
                description=row['description']
            )
            created_types[product_type.label] = product_type  # Use label as key since products.xlsx uses it
        self.stdout.write(f'Created {len(created_types)} product types')

        # Load Products
        df_products = pd.read_excel(os.path.join(dataset_path, 'products.xlsx'))
        created_products = {}
        for _, row in df_products.iterrows():
            product = Product.objects.create(
                code=str(row['code']),
                name=row['name'],
                description=row['description'],
                unit_measure=row['unit_measure'],
                product_type=created_types[row['product_type']]  # Use product_type label to look up
            )
            created_products[product.code] = product
        self.stdout.write(f'Created {len(created_products)} products')

        # Load Carts
        df_carts = pd.read_excel(os.path.join(dataset_path, 'carts.xlsx'))
        created_carts = {}
        for _, row in df_carts.iterrows():
            cart = Cart.objects.create(
                code=row['code'],
                name=row['name'],
                description=row['description']
            )
            created_carts[str(row['id'])] = cart  # Use id as key since cart_products.xlsx uses it
        self.stdout.write(f'Created {len(created_carts)} carts')

        # Load Cart Products
        df_cart_products = pd.read_excel(os.path.join(dataset_path, 'cart_products.xlsx'))
        
        # Define quarterly periods for 2025
        date_ranges = [
            ('2025-01-01', '2025-03-31'),  # Q1
            ('2025-04-01', '2025-06-30'),  # Q2
            ('2025-07-01', '2025-09-30'),  # Q3
            ('2025-10-01', '2025-12-31'),  # Q4
        ]
        
        # Special periods
        special_periods = {
            'ramadan': ('2025-03-01', '2025-03-31'),  # Ramadan period
            'summer': ('2025-06-15', '2025-09-15'),   # Summer period
            'winter': ('2025-11-15', '2025-02-15'),   # Winter period
        }
        
        for _, row in df_cart_products.iterrows():
            cart_id = str(row['cart_id'])
            
            # Choose date range based on cart type
            if cart_id in ['18']:  # Ramadan cart
                date_from, date_to = special_periods['ramadan']
            elif cart_id in ['9']:  # Gift cart - longer availability
                date_from, date_to = '2025-01-01', '2025-12-31'
            elif cart_id in ['22']:  # Eco cart - quarterly rotation
                quarter = int((pd.to_datetime('2025-02-02').month - 1) / 3)
                date_from, date_to = date_ranges[quarter]
            else:
                # Randomly assign one of the quarterly periods for other carts
                date_from, date_to = date_ranges[hash(cart_id) % len(date_ranges)]
            
            CartProducts.objects.create(
                id=f"CP_{row['cart_id']}_{row['product_code']}",
                product=created_products[str(row['product_code'])],
                cart=created_carts[cart_id],
                weight=row['weight'],
                date_from=pd.to_datetime(date_from).date(),
                date_to=pd.to_datetime(date_to).date()
            )
        
        self.stdout.write(f'Created {len(df_cart_products)} cart products')

        # Load Product Prices
        df_product_prices = pd.read_excel(os.path.join(dataset_path, 'product_prices.xlsx'))
        for _, row in df_product_prices.iterrows():
            ProductPrice.objects.create(
                value=row['price'],
                date_from=pd.to_datetime(row['start_date']).date(),
                date_to=pd.to_datetime(row['end_date']).date(),
                product=created_products[str(row['product_code'])],
                point_of_sale=created_points_of_sale['1']  # Use first point of sale as default
            )
        self.stdout.write(f'Created {len(df_product_prices)} product prices')

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from Excel files'))
