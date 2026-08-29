import json, re, io, contextlib
import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from django.conf import settings
settings.ALLOWED_HOSTS.append("testserver")
from django.test import Client
from products.models import Product

c = Client()

# 1. register (activation email prints to console, capture it)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    r = c.post("/api/auth/register/", {"first_name": "Snow", "last_name": "Child",
        "email": "snow@test.com", "password": "TestPass123", "password2": "TestPass123",
        "phone": "01000000000"})
print("register:", r.status_code)
from accounts.models import User
from accounts.tokens import make_token
token = make_token(User.objects.get(email="snow@test.com").id, "activate")

# 2. login before activation should fail
r = c.post("/api/auth/login/", {"email": "snow@test.com", "password": "TestPass123"})
print("login before activation:", r.status_code, "(expect 401)")

# 3. activate then login
r = c.get(f"/api/auth/activate/{token}/")
print("activate:", r.status_code, r.json()["detail"])
r = c.post("/api/auth/login/", {"email": "snow@test.com", "password": "TestPass123"})
print("login after activation:", r.status_code)
access = r.json()["access"]
auth = {"HTTP_AUTHORIZATION": f"Bearer {access}"}

# 4. browse and search products
r = c.get("/api/products/")
print("products list:", r.status_code, "count:", len(r.json()))
r = c.get("/api/products/?search=leather")
print("search 'leather':", [p["title"] for p in r.json()])
r = c.get("/api/products/?category=food")
print("filter food:", [p["title"] for p in r.json()])

# 5. product detail with related + final_price
r = c.get("/api/products/1/")
d = r.json()
print("detail:", d["title"], "| price:", d["price"], "| final:", d["final_price"], "| related:", len(d["related"]))

# 6. customer cannot create a product
r = c.post("/api/products/", {"title": "Hack", "description": "x", "price": 1, "stock": 1, "category_id": 1}, **auth)
print("customer create product:", r.status_code, "(expect 403)")

# 7. seller login and create product
r = c.post("/api/auth/login/", {"email": "seller@mahally.com", "password": "mahally123"})
seller_auth = {"HTTP_AUTHORIZATION": f"Bearer {r.json()['access']}"}
r = c.post("/api/products/", {"title": "Luxor Alabaster Candle Holder", "description": "Carved alabaster.",
    "price": 300, "stock": 10, "category_id": 4, "brand": "Luxor Stone", "tags": "alabaster"}, **seller_auth)
print("seller create product:", r.status_code, "| approved:", r.json().get("is_approved"), "(expect False)")

# 8. customer cannot edit seller's product
r = c.put("/api/products/1/", json.dumps({"title": "Stolen", "description": "x", "price": 1, "stock": 1, "category_id": 1}), content_type="application/json", **auth)
print("customer edit foreign product:", r.status_code, "(expect 403)")

# 9. place an order, check stock decrement + price snapshot
stock_before = Product.objects.get(id=1).stock
r = c.post("/api/orders/", json.dumps({"payment_method": "cod", "address": "12 Tahrir St",
    "city": "Giza", "phone": "01000000000",
    "items": [{"product_id": 1, "quantity": 2}, {"product_id": 5, "quantity": 1}]}),
    content_type="application/json", **auth)
o = r.json()
print("create order:", r.status_code, "| total:", o["total"], "| items:", len(o["items"]))
print("stock 25 -> ", Product.objects.get(id=1).stock, "(expect 23)")

# 10. over-stock order rejected
r = c.post("/api/orders/", json.dumps({"payment_method": "cod", "address": "x", "city": "x",
    "phone": "x", "items": [{"product_id": 4, "quantity": 999}]}), content_type="application/json", **auth)
print("over-stock order:", r.status_code, r.json(), "(expect 400)")

# 11. order history + review + seller endpoints + status update
r = c.get("/api/orders/", **auth)
print("order history:", r.status_code, "orders:", len(r.json()))
r = c.post("/api/products/1/reviews/", {"rating": 5, "comment": "Excellent quality!"}, **auth)
print("post review:", r.status_code)
r = c.get("/api/seller/orders/", **seller_auth)
oid = r.json()[0]["id"]
print("seller orders:", r.status_code, "count:", len(r.json()))
r = c.patch(f"/api/orders/{oid}/status/", json.dumps({"status": "shipped"}), content_type="application/json", **seller_auth)
print("seller update status:", r.status_code, "->", r.json()["status"])

# 12. profile update
r = c.patch("/api/auth/profile/", json.dumps({"first_name": "Snow", "profile": {"city": "Giza", "country": "Egypt"}}), content_type="application/json", **auth)
print("profile update:", r.status_code, "| city:", r.json()["profile"]["city"])
print("\nALL CHECKS DONE")
