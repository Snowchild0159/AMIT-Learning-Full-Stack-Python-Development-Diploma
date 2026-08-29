import { useState } from "react";
import { apiFetch, errorText } from "../api";
import { useAuth } from "../context/AuthContext";

function Profile() {
  const { user, setUser } = useAuth();
  const [form, setForm] = useState({
    first_name: user.first_name || "",
    last_name: user.last_name || "",
    phone: user.phone || "",
    address: user.profile?.address || "",
    birthdate: user.profile?.birthdate || "",
    city: user.profile?.city || "",
    country: user.profile?.country || "",
  });
  const [message, setMessage] = useState("");

  function handleChange(event) {
    setForm({ ...form, [event.target.name]: event.target.value });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    const res = await apiFetch("/api/auth/profile/", {
      method: "PATCH",
      body: {
        first_name: form.first_name,
        last_name: form.last_name,
        phone: form.phone,
        profile: {
          address: form.address,
          birthdate: form.birthdate || null,
          city: form.city,
          country: form.country,
        },
      },
    });
    if (res.ok) {
      setUser(res.data);
      setMessage("Profile saved.");
    } else {
      setMessage(errorText(res.data));
    }
  }

  return (
    <div className="page narrow">
      <h2>My profile</h2>
      <p className="footer-muted">Email: {user.email} (cannot be changed)</p>
      <form className="form" onSubmit={handleSubmit}>
        <label>First name<input name="first_name" value={form.first_name} onChange={handleChange} /></label>
        <label>Last name<input name="last_name" value={form.last_name} onChange={handleChange} /></label>
        <label>Phone<input name="phone" value={form.phone} onChange={handleChange} /></label>
        <label>Address<input name="address" value={form.address} onChange={handleChange} /></label>
        <label>Birthdate<input type="date" name="birthdate" value={form.birthdate || ""} onChange={handleChange} /></label>
        <label>City<input name="city" value={form.city} onChange={handleChange} /></label>
        <label>Country<input name="country" value={form.country} onChange={handleChange} /></label>
        {message && <p className="form-message">{message}</p>}
        <button className="dark-button" type="submit">Save</button>
      </form>
    </div>
  );
}

export default Profile;
