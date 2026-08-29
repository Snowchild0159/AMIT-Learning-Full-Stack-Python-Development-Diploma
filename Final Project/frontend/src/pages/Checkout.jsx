import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { apiFetch, errorText } from "../api";
import { useCart } from "../context/CartContext";
import { useAuth } from "../context/AuthContext";

function Checkout() {
  const { items, subtotal, clearCart } = useCart();
  const { user } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState({
    address: user?.profile?.address || "",
    city: user?.profile?.city || "",
    phone: user?.phone || "",
    payment_method: "cod",
  });
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  function handleChange(event) {
    setForm({ ...form, [event.target.name]: event.target.value });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setSubmitting(true);
    setError("");
    const res = await apiFetch("/api/orders/", {
      method: "POST",
      body: {
        ...form,
        items: items.map((item) => ({ product_id: item.id, quantity: item.quantity })),
      },
    });
    setSubmitting(false);
    if (res.ok) {
      clearCart();
      navigate(`/orders/${res.data.id}`, { state: { justOrdered: true } });
    } else {
      setError(errorText(res.data));
    }
  }

  if (items.length === 0) {
    return <p className="page-message">Your cart is empty.</p>;
  }

  return (
    <div className="page narrow">
      <h2>Checkout</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label>
          Shipping address
          <input name="address" value={form.address} onChange={handleChange} required />
        </label>
        <label>
          City
          <input name="city" value={form.city} onChange={handleChange} required />
        </label>
        <label>
          Phone
          <input name="phone" value={form.phone} onChange={handleChange} required />
        </label>
        <label>
          Payment method
          <select name="payment_method" value={form.payment_method} onChange={handleChange}>
            <option value="cod">Cash on Delivery</option>
            <option value="card">Demo Card Payment</option>
          </select>
        </label>

        <div className="order-summary">
          <h3>Order summary</h3>
          {items.map((item) => (
            <p key={item.id}>
              {item.quantity} × {item.title} — {(item.price * item.quantity).toFixed(2)} EGP
            </p>
          ))}
          <strong>Total: {subtotal.toFixed(2)} EGP</strong>
        </div>

        {error && <p className="form-error">{error}</p>}
        <button className="dark-button" type="submit" disabled={submitting}>
          {submitting ? "Placing order..." : "Place order"}
        </button>
      </form>
    </div>
  );
}

export default Checkout;
