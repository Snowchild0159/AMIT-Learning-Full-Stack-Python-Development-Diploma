from django.core.management.base import BaseCommand
from accounts.models import User, Profile
from products.models import Category, Product


class Command(BaseCommand):
    help = "Fill the database with Egyptian sample data for development"

    def handle(self, *args, **options):
        seller, created = User.objects.get_or_create(
            email="seller@mahally.com",
            defaults={"username": "seller@mahally.com", "first_name": "Omar",
                      "last_name": "Hassan", "phone": "01001234567",
                      "is_seller": True, "is_active": True},
        )
        if created:
            seller.set_password("mahally123")
            seller.save()
            Profile.objects.create(user=seller, city="Cairo")

        customer, created = User.objects.get_or_create(
            email="customer@mahally.com",
            defaults={"username": "customer@mahally.com", "first_name": "Nour",
                      "last_name": "Adel", "phone": "01007654321", "is_active": True},
        )
        if created:
            customer.set_password("mahally123")
            customer.save()
            Profile.objects.create(user=customer, city="Giza")

        categories = {
            "Handmade": "handmade",
            "Clothing": "clothing",
            "Accessories": "accessories",
            "Home": "home",
            "Food": "food",
            "Beauty": "beauty",
        }
        cat_objects = {}
        for name, slug in categories.items():
            cat, _ = Category.objects.get_or_create(name=name, slug=slug)
            cat_objects[slug] = cat

        products = [
            ("Handmade Leather Wallet", "Genuine leather wallet stitched by hand in old Cairo.", 650, "Cairo Craft", "accessories", "leather,handmade,wallet", 25, 10),
            ("Alexandria Cotton Shirt", "Breathable Egyptian cotton shirt, perfect for summer.", 850, "Alex Cotton", "clothing", "cotton,shirt,summer", 40, None),
            ("Siwa Handmade Basket", "Palm leaf basket woven by artisans in Siwa oasis.", 420, "Siwa Hands", "handmade", "basket,palm,handmade", 15, None),
            ("Khan El Khalili Brass Lamp", "Traditional engraved brass lamp with warm light.", 1200, "Khan Crafts", "home", "brass,lamp,traditional", 8, 20),
            ("Aswan Dates Box 1kg", "Premium semi-dry dates from Aswan farms.", 180, "Aswan Farms", "food", "dates,aswan,natural", 60, None),
            ("Nefertiti Silver Necklace", "Sterling silver necklace with Nefertiti pendant.", 950, "Cairo Silver", "accessories", "silver,necklace,pharaonic", 12, 15),
            ("Fayoum Pottery Vase", "Hand-painted clay vase from Fayoum pottery school.", 380, "Fayoum Pottery", "home", "pottery,clay,vase", 20, None),
            ("Shea & Olive Natural Soap", "Handmade soap with olive oil and shea butter.", 95, "Nefertari", "beauty", "soap,natural,handmade", 100, None),
            ("Galabeya Classic Navy", "Comfortable traditional galabeya in navy blue.", 720, "Alex Cotton", "clothing", "galabeya,traditional,cotton", 30, 10),
            ("Sinai Herbal Tea Mix", "Wild herbs from Sinai mountains, 100g pack.", 140, "Sinai Herbs", "food", "tea,herbs,sinai", 45, None),
            ("Mother of Pearl Jewelry Box", "Inlaid wooden box with mother of pearl patterns.", 1600, "Khan Crafts", "handmade", "wood,inlay,box", 6, None),
            ("Egyptian Cotton Towel Set", "Soft 3-piece towel set, 600 GSM.", 540, "Nile Home", "home", "cotton,towels,bathroom", 35, 25),
        ]

        for title, desc, price, brand, cat_slug, tags, stock, discount in products:
            Product.objects.get_or_create(
                title=title,
                defaults={
                    "seller": seller, "category": cat_objects[cat_slug],
                    "description": desc, "price": price, "brand": brand,
                    "tags": tags, "stock": stock, "discount": discount,
                    "is_approved": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Seed data created."))
        self.stdout.write("Seller login: seller@mahally.com / mahally123")
        self.stdout.write("Customer login: customer@mahally.com / mahally123")
