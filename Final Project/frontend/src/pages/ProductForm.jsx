import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { apiFetch, errorText } from "../api";

// one form used for both adding and editing a product
function ProductForm() {
  const { id } = useParams();
  const navigate = useNavigate();
  const editing = Boolean(id);
  const [categories, setCategories] = useState([]);
  const [form, setForm] = useState({
    title: "", description: "", price: "", stock: "",
    brand: "", tags: "", discount: "", category_id: "",
  });
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      const catRes = await apiFetch("/api/categories/");
      if (catRes.ok) setCategories(catRes.data);
      if (editing) {
        const res = await apiFetch(`/api/products/${id}/`);
        if (res.ok) {
          const p = res.data;
          setForm({
            title: p.title, description: p.description, price: p.price,
            stock: p.stock, brand: p.brand, tags: p.tags,
            discount: p.discount || "", category_id: p.category.id,
          });
        }
      }
    }
    load();
  }, [id]);

  function handleChange(event) {
    setForm({ ...form, [event.target.name]: event.target.value });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    const body = { ...form, discount: form.discount === "" ? null : Number(form.discount) };
    const res = editing
      ? await apiFetch(`/api/products/${id}/`, { method: "PUT", body })
      : await apiFetch("/api/products/", { method: "POST", body });
    if (res.ok) {
      navigate("/seller");
    } else {
      setError(errorText(res.data));
    }
  }

  return (
    <div className="page narrow">
      <h2>{editing ? "Edit product" : "Add product"}</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label>Title<input name="title" value={form.title} onChange={handleChange} required /></label>
        <label>Description<textarea name="description" rows="4" value={form.description} onChange={handleChange} required /></label>
        <label>Price (EGP)<input type="number" step="0.01" name="price" value={form.price} onChange={handleChange} required /></label>
        <label>Stock quantity<input type="number" name="stock" value={form.stock} onChange={handleChange} required /></label>
        <label>
          Category
          <select name="category_id" value={form.category_id} onChange={handleChange} required>
            <option value="">Choose...</option>
            {categories.map((cat) => (
              <option key={cat.id} value={cat.id}>{cat.name}</option>
            ))}
          </select>
        </label>
        <label>Brand<input name="brand" value={form.brand} onChange={handleChange} /></label>
        <label>Tags (comma separated)<input name="tags" value={form.tags} onChange={handleChange} placeholder="leather,handmade" /></label>
        <label>Discount % (optional)<input type="number" name="discount" value={form.discount} onChange={handleChange} min="0" max="90" /></label>
        <p className="footer-muted">
          Product images are uploaded through the Django Admin for now.
          New products appear publicly after admin approval.
        </p>
        {error && <p className="form-error">{error}</p>}
        <button className="dark-button" type="submit">{editing ? "Save changes" : "Create product"}</button>
      </form>
    </div>
  );
}

export default ProductForm;
