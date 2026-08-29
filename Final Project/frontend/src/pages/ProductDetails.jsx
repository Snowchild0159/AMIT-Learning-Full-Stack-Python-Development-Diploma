import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { apiFetch, errorText } from "../api";
import { useCart } from "../context/CartContext";
import { useAuth } from "../context/AuthContext";
import ProductCard from "../components/ProductCard";

function ProductDetails() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [quantity, setQuantity] = useState(1);
  const [imageIndex, setImageIndex] = useState(0);
  const [rating, setRating] = useState(5);
  const [comment, setComment] = useState("");
  const [message, setMessage] = useState("");
  const { addItem } = useCart();
  const { user } = useAuth();

  async function fetchProduct() {
    const res = await apiFetch(`/api/products/${id}/`);
    if (res.ok) setProduct(res.data);
  }

  useEffect(() => {
    fetchProduct();
    setImageIndex(0);
    setMessage("");
    window.scrollTo(0, 0);
  }, [id]);

  if (!product) return <p className="page-message">Loading...</p>;

  async function handleReview(event) {
    event.preventDefault();
    const res = await apiFetch(`/api/products/${id}/reviews/`, {
      method: "POST",
      body: { rating, comment },
    });
    if (res.ok) {
      setComment("");
      setMessage("Review added, thank you!");
      fetchProduct();
    } else {
      setMessage(errorText(res.data));
    }
  }

  const images = product.images || [];

  return (
    <div className="details">
      <div className="details-top">
        <div className="details-images">
          {images.length > 0 ? (
            <>
              <img src={images[imageIndex].image} alt={product.title} />
              {images.length > 1 && (
                <div className="thumbs">
                  {images.map((img, index) => (
                    <img
                      key={img.id}
                      src={img.image}
                      alt=""
                      className={index === imageIndex ? "selected" : ""}
                      onClick={() => setImageIndex(index)}
                    />
                  ))}
                </div>
              )}
            </>
          ) : (
            <div className="image-placeholder big">{product.title[0]}</div>
          )}
        </div>

        <div className="details-info">
          <h2>{product.title}</h2>
          <p className="card-brand">
            {product.brand} • {product.category?.name}
            {product.average_rating && ` • ★ ${product.average_rating}`}
          </p>
          <p className="details-price">
            {product.discount ? (
              <span className="old-price">{product.price} EGP</span>
            ) : null}
            {product.final_price} EGP
          </p>
          <p>{product.description}</p>
          <p className={product.stock > 0 ? "in-stock" : "out-stock"}>
            {product.stock > 0 ? `${product.stock} in stock` : "Out of stock"}
          </p>

          {product.stock > 0 && (
            <div className="add-row">
              <input
                type="number"
                min="1"
                max={product.stock}
                value={quantity}
                onChange={(event) => setQuantity(Number(event.target.value))}
              />
              <button
                className="dark-button"
                onClick={() => addItem(product, quantity)}
              >
                Add to Cart
              </button>
            </div>
          )}
        </div>
      </div>

      <section className="reviews">
        <h3>Reviews ({product.reviews.length})</h3>
        {product.reviews.map((review) => (
          <div key={review.id} className="review">
            <strong>{review.user_name}</strong> — {"★".repeat(review.rating)}
            <p>{review.comment}</p>
          </div>
        ))}
        {product.reviews.length === 0 && <p className="footer-muted">No reviews yet.</p>}

        {user ? (
          <form className="review-form" onSubmit={handleReview}>
            <select value={rating} onChange={(event) => setRating(Number(event.target.value))}>
              {[5, 4, 3, 2, 1].map((value) => (
                <option key={value} value={value}>{value} stars</option>
              ))}
            </select>
            <textarea
              rows="3"
              placeholder="Your review"
              value={comment}
              onChange={(event) => setComment(event.target.value)}
            />
            <button className="dark-button" type="submit">Post review</button>
            {message && <p className="form-message">{message}</p>}
          </form>
        ) : (
          <p className="footer-muted">
            <Link to="/login">Log in</Link> to write a review.
          </p>
        )}
      </section>

      {product.related.length > 0 && (
        <section>
          <h3>Related products</h3>
          <div className="product-grid">
            {product.related.map((item) => (
              <ProductCard key={item.id} product={item} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

export default ProductDetails;
