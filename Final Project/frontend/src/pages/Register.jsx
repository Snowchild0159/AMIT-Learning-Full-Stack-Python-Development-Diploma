import { useState } from "react";
import { Link } from "react-router-dom";
import { host, errorText } from "../api";

function Register() {
  const [form, setForm] = useState({
    first_name: "", last_name: "", email: "",
    password: "", password2: "", phone: "",
  });
  const [photo, setPhoto] = useState(null);
  const [error, setError] = useState("");
  const [done, setDone] = useState(false);

  function handleChange(event) {
    setForm({ ...form, [event.target.name]: event.target.value });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    // FormData because the profile photo is a file
    const data = new FormData();
    Object.entries(form).forEach(([key, value]) => data.append(key, value));
    if (photo) data.append("photo", photo);

    const response = await fetch(`${host}/api/auth/register/`, {
      method: "POST",
      body: data,
    });
    const resData = await response.json().catch(() => null);
    if (response.ok) {
      setDone(true);
    } else {
      setError(errorText(resData));
    }
  }

  if (done) {
    return (
      <div className="page narrow">
        <div className="success-banner">
          Account created! Check your email for the activation link
          (valid for 24 hours). In development, the email prints in the
          Django terminal.
        </div>
        <Link to="/login">Go to login</Link>
      </div>
    );
  }

  return (
    <div className="page narrow">
      <h2>Register</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label>First name<input name="first_name" value={form.first_name} onChange={handleChange} required /></label>
        <label>Last name<input name="last_name" value={form.last_name} onChange={handleChange} required /></label>
        <label>Email<input type="email" name="email" value={form.email} onChange={handleChange} required /></label>
        <label>Password<input type="password" name="password" value={form.password} onChange={handleChange} required /></label>
        <label>Confirm password<input type="password" name="password2" value={form.password2} onChange={handleChange} required /></label>
        <label>Mobile phone<input name="phone" value={form.phone} onChange={handleChange} required /></label>
        <label>Profile photo (optional)<input type="file" accept="image/*" onChange={(event) => setPhoto(event.target.files[0])} /></label>
        {error && <p className="form-error">{error}</p>}
        <button className="dark-button" type="submit">Create account</button>
      </form>
      <p className="footer-muted">Already registered? <Link to="/login">Login</Link></p>
    </div>
  );
}

export default Register;
