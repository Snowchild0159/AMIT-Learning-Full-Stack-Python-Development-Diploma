import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { apiFetch } from "../api";

function Orders() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchOrders() {
      const res = await apiFetch("/api/orders/");
      if (res.ok) setOrders(res.data);
      setLoading(false);
    }
    fetchOrders();
  }, []);

  if (loading) return <p className="page-message">Loading...</p>;

  return (
    <div className="page">
      <h2>Order history</h2>
      {orders.length === 0 && <p className="page-message">No orders yet.</p>}
      {orders.map((order) => (
        <Link key={order.id} to={`/orders/${order.id}`} className="order-row">
          <span>Order #{order.id}</span>
          <span className={`status status-${order.status}`}>{order.status}</span>
          <span>{order.items.length} item(s)</span>
          <strong>{order.total} EGP</strong>
        </Link>
      ))}
    </div>
  );
}

export default Orders;
