import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { apiFetch } from "../api";

function Sidebar({ open, onClose }) {
  const [categories, setCategories] = useState([]);
  const [searchParams] = useSearchParams();
  const active = searchParams.get("category");

  useEffect(() => {
    async function fetchCategories() {
      const res = await apiFetch("/api/categories/");
      if (res.ok) setCategories(res.data);
    }
    fetchCategories();
  }, []);

  return (
    <>
      <div className={`overlay ${open ? "show" : ""}`} onClick={onClose}></div>
      <aside className={`sidebar ${open ? "open" : ""}`} aria-label="Categories">
        <nav>
          <ul className="cat-list">
            <li className={!active ? "active" : ""}>
              <Link to="/" onClick={onClose}>All products</Link>
            </li>
            {categories.map((cat) => (
              <li key={cat.id} className={active === cat.slug ? "active" : ""}>
                <Link to={`/?category=${cat.slug}`} onClick={onClose}>
                  {cat.name}
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      </aside>
    </>
  );
}

export default Sidebar;
