# Mahally — Frontend

React (Vite) frontend for the Mahally marketplace. Design converted from my
original HTML/CSS (SnowJeansOVO.html + snow-style.css) into React components.

## Setup
```
npm install
npm run dev
```
Opens on http://localhost:5173 — the Django backend must be running on port 8000.

## Structure
```
src/
  api.js                  fetch helper (attaches JWT token)
  context/AuthContext.jsx login state shared across the app
  context/CartContext.jsx cart state, saved in localStorage
  components/             Navbar, Sidebar, Hero, ProductCard, Footer, ProtectedRoute
  pages/                  Home, ProductDetails, Cart, Checkout, Orders, OrderDetails,
                          Login, Register, Activate, ResetPassword, Profile,
                          SellerDashboard, ProductForm
  styles.css              evolved from my snow-style.css
```

## Test flow
1. Log in as customer@mahally.com / mahally123
2. Add products to cart, checkout with Cash on Delivery
3. See the order in Order history
4. Log in as seller@mahally.com / mahally123 → Dashboard → update order status
