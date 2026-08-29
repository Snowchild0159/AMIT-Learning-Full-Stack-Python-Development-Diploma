import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { apiFetch } from "../api";
import Hero from "../components/Hero";
import ProductCard from "../components/ProductCard";

function Home() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [ordering, setOrdering] = useState("");
  const [searchParams] = useSearchParams();
  const search = searchParams.get("search") || "";
  const category = searchParams.get("category") || "";

  useEffect(() => {
    async function fetchProducts() {
      setLoading(true);
      const params = new URLSearchParams();
      if (search) params.set("search", search);
      if (category) params.set("category", category);
      if (ordering) params.set("ordering", ordering);
      const res = await apiFetch(`/api/products/?${params.toString()}`);
      if (res.ok) setProducts(res.data);
      setLoading(false);
    }
    fetchProducts();
  }, [search, category, ordering]);

  return (
    <div>
      {!search && !category && <Hero />}

      <div className="grid-toolbar">
        <span className="items-count">
          {loading ? "Loading..." : `${products.length} items`}
          {search && ` for "${search}"`}
        </span>
        <select value={ordering} onChange={(event) => setOrdering(event.target.value)}>
          <option value="">Newest</option>
          <option value="price">Price: low to high</option>
          <option value="-price">Price: high to low</option>
        </select>
      </div>

      <section className="product-grid" id="grid" aria-label="Products">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </section>
      {!loading && products.length === 0 && (
        <p className="page-message">No products found.</p>
      )}

      <div className="divider"></div>

      <section className="subscribe">
        <div className="subscribe-inner">
          <h2>Subscribe</h2>
          <p>Special offers from Egyptian local brands:</p>
          <form onSubmit={(event) => event.preventDefault()}>
            <input type="email" placeholder="Enter e-mail" required />
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </section>
    </div>
  );
}

export default Home;
