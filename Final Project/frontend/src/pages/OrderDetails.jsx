import { useEffect, useState } from "react";
import { useParams, useLocation } from "react-router-dom";
import { apiFetch } from "../api";

function OrderDetails() {
  const { id } = useParams();
  const location = useLocation();
  const [order, setOrder] = useState(null);
  const justOrdered = location.state?.justOrdered;

  useEffect(() => {
    async function fetchOrder() {
      const res = await apiFetch(`/api/orders/${id}/`);
      if (res.ok) setOrder(res.data);
    }
    fetchOrder();
  }, [id]);

  if (!order) return <p className="page-message">Loading...</p>;

  return (
    <div className="page narrow">
      {justOrdered && (
        <div className="success-banner">Order placed successfully. Thank you!</div>
      )}
      <h2>Order #{order.id}</h2>
      <p>
        Status: <span className={`status status-${order.status}`}>{order.status}</span>
      </p>
      <p className="footer-muted">
        {order.address}, {order.city} — {order.phone} •{" "}
        {order.payment_method === "cod" ? "Cash on Delivery" : "Demo Card"}
      </p>
      <div className="order-summary">
        {order.items.map((item, index) => (
          <p key={index}>
            {item.quantity} × {item.title} — {item.price} EGP each
          </p>
        ))}
        <strong>Total: {order.total} EGP</strong>
      </div>
    </div>
  );
}

export default OrderDetails;
