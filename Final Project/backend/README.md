# Mahally — Backend

Egyptian local-business marketplace. Final project for the AMIT Full Stack Python Development Diploma.

Django + Django REST Framework + PostgreSQL (SQLite fallback for quick local runs).

## Setup

```
python -m venv venv
venv\Scripts\activate        (Windows)   |   source venv/bin/activate  (Mac/Linux)
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver
```

To use PostgreSQL instead of SQLite, create a database named `mahally` and run with:
```
USE_POSTGRES=1 DB_USER=postgres DB_PASSWORD=yourpass python manage.py runserver
```

Activation and password-reset emails print to the terminal (console email backend).

## Test accounts (from seed_data)
- Seller: seller@mahally.com / mahally123
- Customer: customer@mahally.com / mahally123

## API overview
```
POST /api/auth/register/                POST /api/auth/login/
GET  /api/auth/activate/<token>/        GET/PATCH /api/auth/profile/
POST /api/auth/password-reset/          POST /api/auth/password-reset/confirm/

GET  /api/categories/
GET  /api/products/?search=&category=&ordering=
GET/PUT/DELETE /api/products/<id>/      POST /api/products/
GET/POST /api/products/<id>/reviews/

POST /api/orders/     GET /api/orders/     GET /api/orders/<id>/
PATCH /api/orders/<id>/status/
GET /api/seller/products/    GET /api/seller/orders/
```

Run `python smoke_test.py` to test the whole flow end to end.
