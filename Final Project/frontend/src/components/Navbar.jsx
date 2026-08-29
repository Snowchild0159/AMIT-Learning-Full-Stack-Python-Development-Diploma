import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useCart } from "../context/CartContext";

function Navbar({ onBurgerClick }) {
  const { user, logout } = useAuth();
  const { count } = useCart();
  const navigate = useNavigate();
  const [search, setSearch] = useState("");

  function handleSearch(event) {
    event.preventDefault();
    navigate(search ? `/?search=${encodeURIComponent(search)}` : "/");
  }

  return (
    <header className="topbar">
      <div className="topbar-inner">
        <button className="burger" aria-label="Toggle menu" onClick={onBurgerClick}>
          <span></span>
          <span></span>
          <span></span>
        </button>

        <Link to="/" className="logo">
          Mahally <span className="logo-ar">محلّي</span>
        </Link>

        <form className="search-form" onSubmit={handleSearch}>
          <input
            type="text"
            placeholder="Search products, brands, tags..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </form>

        <nav className="topbar-links">
          {user ? (
            <>
              {user.is_seller && <Link to="/seller">Dashboard</Link>}
              <Link to="/orders">Orders</Link>
              <Link to="/profile">{user.first_name || "Profile"}</Link>
              <button className="link-button" onClick={logout}>Logout</button>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
          <Link to="/cart" className="cart-link" aria-label="Cart">
            🛒{count > 0 && <span className="cart-count">{count}</span>}
          </Link>
        </nav>
      </div>
    </header>
  );
}

export default Navbar;
