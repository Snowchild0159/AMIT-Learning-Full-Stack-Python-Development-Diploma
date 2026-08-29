import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { apiFetch } from "../api";
import { useAuth } from "../context/AuthContext";

function SellerDashboard() {
  const { user } = useAuth();
  const [products, setProducts] = useState([]);
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  async function fetchData() {
    const [productsRes, ordersRes] = await Promise.all([
      apiFetch("/api/seller/products/"),
      apiFetch("/api/seller/orders/"),
    ]);
    if (productsRes.ok) setProducts(productsRes.data);
    if (ordersRes.ok) setOrders(ordersRes.data);
    setLoading(false);
  }

  useEffect(() => {
    fetchData();
  }, []);

  async function handleDelete(id) {
    if (!confirm("Delete this product?")) return;
    const res = await apiFetch(`/api/products/${id}/`, { method: "DELETE" });
    if (res.ok || res.status === 204) fetchData();
  }

  async function handleStatus(orderId, status) {
    await apiFetch(`/api/orders/${orderId}/status/`, {
      method: "PATCH",
      body: { status },
    });
    fetchData();
  }

  if (!user.is_seller) {
    return <p className="page-message">This page is for sellers only.</p>;
  }
  if (loading) return <p className="page-message">Loading...</p>;

  const revenue = orders.reduce((sum, order) => sum + Number(order.total), 0);

  return (
    <div className="page">
      <h2>Seller dashboard</h2>

      <div className="stats-row">
        <div className="stat-box">Products<strong>{products.length}</strong></div>
        <div className="stat-box">Orders<strong>{orders.length}</strong></div>
        <div className="stat-box">Revenue<strong>{revenue.toFixed(0)} EGP</strong></div>
      </div>

      <div className="section-header">
        <h3>My products</h3>
        <Link className="dark-button" to="/seller/new">+ Add product</Link>
      </div>
      <div className="seller-table">
        {products.map((product) => (
          <div key={product.id} className="seller-row">
            <span>{product.title}</span>
            <span>{product.final_price} EGP</span>
            <span>stock: {product.stock}</span>
            <span className="footer-muted">
              {/* is_approved is not in the list serializer, so check via detail if needed */}
            </span>
            <Link to={`/seller/edit/${product.id}`}>Edit</Link>
            <button className="remove-button" onClick={() => handleDelete(product.id)}>Delete</button>
          </div>
        ))}
        {products.length === 0 && <p className="page-message">No products yet.</p>}
      </div>

      <h3>Orders with my products</h3>
      {orders.map((order) => (
        <div key={order.id} className="seller-row">
          <span>Order #{order.id}</span>
          <span className={`status status-${order.status}`}>{order.status}</span>
          <span>{order.total} EGP</span>
          <select
            value={order.status}
            onChange={(event) => handleStatus(order.id, event.target.value)}
          >
            <option value="pending">Pending</option>
            <option value="processing">Processing</option>
            <option value="shipped">Shipped</option>
            <option value="delivered">Delivered</option>
          </select>
        </div>
      ))}
      {orders.length === 0 && <p className="page-message">No orders yet.</p>}
    </div>
  );
}

export default SellerDashboard;
