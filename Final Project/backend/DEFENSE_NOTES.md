# Defense notes — what to understand and say

Read this before your presentation. Every point maps to code you can open and show.

## Architecture
Three Django apps: `accounts` (who you are), `products` (what is sold), `orders`
(what was bought). Each app owns its models, serializers, views, urls. React talks
to Django only through the REST API — JSON in, JSON out.

## Authentication (accounts/)
- Custom `User` extends `AbstractUser`; `USERNAME_FIELD = "email"` makes login use
  email instead of username. (accounts/models.py)
- New users are created with `is_active=False`. The login endpoint rejects inactive
  users automatically — that is how "activate before login" is enforced.
- Activation link: `accounts/tokens.py` uses Django's `signing` module. The token
  contains the user id + a cryptographic signature. `signing.loads(max_age=86400)`
  rejects it after 24 hours. No token table needed — say this in the defense.
- Login returns two JWTs (SimpleJWT): a short-lived access token sent as
  `Authorization: Bearer <token>` on every request, and a refresh token to get a
  new access token. The server stays stateless — no sessions.
- Password reset reuses the same signing idea with purpose="reset". The endpoint
  answers the same whether the email exists or not, so attackers can't probe emails.

## Key model decisions
- `BaseModel` (created_at/updated_at/is_deleted) is abstract — every table gets the
  columns, no extra table exists. Products are soft-deleted so old orders keep working.
- `is_seller` is a boolean, not a separate table: a seller IS a user with one extra power.
- `OrderItem.price` is a snapshot of the price at purchase time. If the seller changes
  the price later, order history stays historically true.
- `discount` is a percentage; `final_price()` computes it on the fly — derived values
  are never stored, so they can't go stale.
- `on_delete=PROTECT` on OrderItem.product: you can't hard-delete a product that
  appears in an order (that's also why soft delete exists).

## Permissions (products/permissions.py) — expect a question here
- `IsSellerOrReadOnly`: anyone can GET, only `is_seller` users can POST.
- `IsOwnerOrReadOnly.has_object_permission`: `obj.seller == request.user` — this
  single line is what stops seller A from editing seller B's products.
- Order queryset is always filtered by `user=self.request.user`, so you can never
  read someone else's orders — filtering the queryset IS the security.

## Orders (orders/serializers.py) — the hardest code in the project
`OrderCreateSerializer.create` runs inside `transaction.atomic()`:
1. create the Order
2. for each cart item: lock the product row (`select_for_update`), check stock,
   create OrderItem with the snapshot price, decrease stock
3. save the total
If ANY item fails (e.g. not enough stock), the transaction rolls back and nothing
is saved — no half-orders, no lost stock. "Atomic = all or nothing."

## Search & filtering
DRF `SearchFilter` with `search_fields = ["title", "tags", "brand"]` gives
`?search=leather` (case-insensitive contains). Category filtering is a simple
`queryset.filter(category__slug=...)` in `get_queryset`. Tags are a plain text
field searched with the same mechanism — simple and enough.

## Admin
Django's built-in admin manages users, categories, products, orders. The Product
admin has bulk "Approve/Reject" actions — new seller products start with
`is_approved=False` and only appear publicly after approval.

## Likely questions, short answers
- Why DRF? React needs JSON, not HTML pages; DRF handles serialization,
  validation, auth and permissions for APIs.
- Why JWT and not sessions? The frontend is a separate app on a different port;
  tokens keep the API stateless and avoid cookie/CSRF complexity for the SPA.
- What is a serializer? Translator between model instances and JSON, plus
  validation of incoming data.
- What is a foreign key? A column pointing at another table's primary key —
  Product.seller_id points at a row in the users table.
- Why PostgreSQL? Relational data (users→orders→items) with real constraints,
  transactions and concurrent access; the course database.
- How is the project secured? Passwords hashed by set_password, JWT auth,
  permission classes, per-user querysets, admin-only approval.

## Frontend (React) — what to understand
- The design journey: I built the layout first in plain HTML/CSS (sticky topbar,
  burger + off-canvas sidebar, category list with the orange active marker,
  product grid, black subscribe band, gray footer). Then I converted each section
  into a React component and renamed classes to semantic names. Same design
  language, now data-driven.
- Components vs pages: components are reusable pieces (Navbar, ProductCard),
  pages are what React Router mounts for each URL.
- React Router: `<Routes>` maps paths to pages; `useParams` reads `/product/:id`;
  `<Navigate>` inside ProtectedRoute redirects logged-out users to /login.
- Context: two only. AuthContext (current user + login/logout) and CartContext
  (items + totals). Everything else is local useState — Context only where many
  components need the same state.
- Cart architecture: the cart is ONLY in localStorage (works for guests, survives
  refresh). The backend never stores carts; it validates stock when the order is
  actually created. Simplest design that satisfies the requirement.
- api.js: one fetch wrapper adds `Authorization: Bearer <token>` and JSON headers
  everywhere — instead of repeating that code in every page.
- useEffect: pages fetch data on mount; Home re-fetches when search/category/
  ordering change (they're in the dependency array).
- Controlled forms: every input's value comes from state and onChange updates it —
  React owns the form data, which makes validation and submission simple.
- Burger menu: my original vanilla JS classList.toggle became a `sidebarOpen`
  useState in App.jsx — same behavior, React-style.
- Product images: uploaded via Django Admin (ProductImage inline). The frontend
  shows a letter placeholder when a product has no image yet.
