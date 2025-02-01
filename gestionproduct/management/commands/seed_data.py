from django.core.management.base import BaseCommand
from django.utils import timezone
from gestionproduct.models import (
    INPC, ProductType, Product, Cart, Wilaya, 
    Moughataa, Commune, PointOfSale, ProductPrice, CartProducts
)
from datetime import date, timedelta
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seeds the database with initial test data using Faker'

    def __init__(self):
        super().__init__()
        self.fake = Faker()
        # Set a fixed seed for reproducible results
        Faker.seed(12345)
        random.seed(12345)

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

        self.stdout.write('Seeding new data...')

        # Create INPC data for the last 12 months
        current_year = timezone.now().year
        base_inpc = 100.0
        for month in range(1, 13):
            fluctuation = random.uniform(-2, 2)
            INPC.objects.create(
                year=current_year,
                month=month,
                inpc_value=round(base_inpc + fluctuation, 2)
            )
            base_inpc += random.uniform(0.3, 0.8)  # Slight increase trend

        # Create Product Types
        product_types = [
            ('FOOD', 'Food Products', 'Basic food and grocery items'),
            ('HYGIENE', 'Hygiene Products', 'Personal care and cleaning items'),
            ('HOUSE', 'Household Items', 'Basic household necessities'),
        ]
        created_types = {}
        for code, label, desc in product_types:
            pt = ProductType.objects.create(
                code=code,
                label=label,
                description=desc
            )
            created_types[code] = pt

        # Create Products
        products_data = [
            ('Rice', 'kg', 'FOOD'),
            ('Flour', 'kg', 'FOOD'),
            ('Sugar', 'kg', 'FOOD'),
            ('Oil', 'L', 'FOOD'),
            ('Soap', 'unit', 'HYGIENE'),
            ('Detergent', 'kg', 'HYGIENE'),
            ('Matches', 'box', 'HOUSE'),
            ('Salt', 'kg', 'FOOD'),
        ]
        created_products = []
        for name, unit, type_code in products_data:
            product = Product.objects.create(
                code=f"{type_code}_{self.fake.unique.random_number(5)}",
                name=name,
                description=self.fake.sentence(),
                unit_measure=unit,
                product_type=created_types[type_code]
            )
            created_products.append(product)

        # Create Carts
        cart_types = ['Basic', 'Family', 'Premium']
        created_carts = []
        for cart_type in cart_types:
            cart = Cart.objects.create(
                code=f"CART_{self.fake.unique.random_number(5)}",
                name=f"{cart_type} Cart",
                description=self.fake.sentence()
            )
            created_carts.append(cart)

        # Create Wilayas
        wilayas = [
            ('NK', 'Nouakchott'),
            ('ND', 'Nouadhibou'),
            ('RS', 'Rosso'),
        ]
        created_wilayas = {}
        for code, name in wilayas:
            wilaya = Wilaya.objects.create(code=code, name=name)
            created_wilayas[code] = wilaya

        # Create Moughataas (3 per Wilaya)
        created_moughataas = {}
        for wilaya_code, wilaya in created_wilayas.items():
            for i in range(3):
                moughataa = Moughataa.objects.create(
                    code=f"{wilaya_code}_M{i+1}",
                    label=f"{self.fake.city()} District",
                    wilaya=wilaya
                )
                created_moughataas[moughataa.code] = moughataa

        # Create Communes (2 per Moughataa)
        created_communes = []
        for moughataa_code, moughataa in created_moughataas.items():
            for i in range(2):
                commune = Commune.objects.create(
                    code=f"{moughataa_code}_C{i+1}",
                    name=self.fake.city(),
                    moughataa=moughataa
                )
                created_communes.append(commune)

        # Create Points of Sale (2-3 per Commune)
        created_pos = []
        pos_types = ['Market', 'Supermarket', 'Corner Store']
        for commune in created_communes:
            for _ in range(random.randint(2, 3)):
                pos = PointOfSale.objects.create(
                    code=f"POS_{self.fake.unique.random_number(5)}",
                    type=random.choice(pos_types),
                    # Approximate coordinates for Mauritania
                    gps_lat=random.uniform(16.0, 20.0),
                    gps_lon=random.uniform(-17.0, -15.0),
                    commune=commune
                )
                created_pos.append(pos)

        # Create Product Prices
        start_date = date(current_year, 1, 1)
        end_date = date(current_year, 12, 31)
        
        for product in created_products:
            base_price = random.uniform(20, 200)
            for pos in created_pos:
                # Add some price variation per location
                price_variation = random.uniform(-10, 10)
                ProductPrice.objects.create(
                    value=round(base_price + price_variation, 2),
                    date_from=start_date,
                    date_to=end_date,
                    product=product,
                    point_of_sale=pos
                )

        # Create Cart Products
        for cart in created_carts:
            # Add 4-6 random products to each cart
            for product in random.sample(created_products, random.randint(4, 6)):
                CartProducts.objects.create(
                    id=f"CP_{self.fake.unique.random_number(5)}",
                    product=product,
                    cart=cart,
                    weight=round(random.uniform(0.5, 5.0), 2),
                    date_from=start_date,
                    date_to=end_date
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with realistic test data'))
