import { Link, useNavigate } from "react-router-dom";
import { useCart } from "../context/CartContext";

function Cart() {
  const { items, updateQuantity, removeItem, subtotal } = useCart();
  const navigate = useNavigate();

  if (items.length === 0) {
    return (
      <div className="page">
        <h2>Your cart</h2>
        <p className="page-message">
          Cart is empty. <Link to="/">Browse products</Link>
        </p>
      </div>
    );
  }

  return (
    <div className="page">
      <h2>Your cart</h2>
      <div className="cart-list">
        {items.map((item) => (
          <div key={item.id} className="cart-item">
            {item.image ? (
              <img src={item.image} alt={item.title} />
            ) : (
              <div className="image-placeholder small">{item.title[0]}</div>
            )}
            <div className="cart-item-info">
              <Link to={`/product/${item.id}`}>{item.title}</Link>
              <p className="footer-muted">{item.price} EGP each</p>
            </div>
            <div className="qty-controls">
              <button onClick={() => updateQuantity(item.id, item.quantity - 1)}>−</button>
              <span>{item.quantity}</span>
              <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>+</button>
            </div>
            <strong>{(item.price * item.quantity).toFixed(2)} EGP</strong>
            <button className="remove-button" onClick={() => removeItem(item.id)}>✕</button>
          </div>
        ))}
      </div>
      <div className="cart-summary">
        <p>Subtotal: <strong>{subtotal.toFixed(2)} EGP</strong></p>
        <p className="footer-muted">Shipping calculated at checkout (free in demo).</p>
        <button className="dark-button" onClick={() => navigate("/checkout")}>
          Proceed to checkout
        </button>
      </div>
    </div>
  );
}

export default Cart;
