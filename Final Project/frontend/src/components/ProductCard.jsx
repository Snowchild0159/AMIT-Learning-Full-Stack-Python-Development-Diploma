import { Link } from "react-router-dom";

function ProductCard({ product }) {
  return (
    <article className="product-card">
      {product.discount ? <div className="badge sale">-{product.discount}%</div> : null}
      <Link to={`/product/${product.id}`}>
        {product.image ? (
          <img src={product.image} alt={product.title} />
        ) : (
          <div className="image-placeholder">{product.title[0]}</div>
        )}
      </Link>
      <h3>
        <Link to={`/product/${product.id}`}>{product.title}</Link>
      </h3>
      <p className="card-brand">{product.brand}</p>
      <p className="card-price">
        {product.discount ? <span className="old-price">{product.price} EGP</span> : null}
        {product.final_price} EGP
      </p>
    </article>
  );
}

export default ProductCard;
