import { useState } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";
import { apiFetch, errorText } from "../api";

// one page, two modes: request a link (no token) or set a new password (token in URL)
function ResetPassword() {
  const { token } = useParams();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  async function handleRequest(event) {
    event.preventDefault();
    const res = await apiFetch("/api/auth/password-reset/", {
      method: "POST",
      body: { email },
    });
    setMessage(res.data?.detail || errorText(res.data));
  }

  async function handleConfirm(event) {
    event.preventDefault();
    const res = await apiFetch("/api/auth/password-reset/confirm/", {
      method: "POST",
      body: { token, password },
    });
    if (res.ok) {
      navigate("/login");
    } else {
      setMessage(errorText(res.data));
    }
  }

  return (
    <div className="page narrow">
      <h2>Reset password</h2>
      {token ? (
        <form className="form" onSubmit={handleConfirm}>
          <label>
            New password
            <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} required />
          </label>
          {message && <p className="form-error">{message}</p>}
          <button className="dark-button" type="submit">Change password</button>
        </form>
      ) : (
        <form className="form" onSubmit={handleRequest}>
          <label>
            Your email
            <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required />
          </label>
          {message && <p className="form-message">{message}</p>}
          <button className="dark-button" type="submit">Send reset link</button>
        </form>
      )}
      <p className="footer-muted"><Link to="/login">Back to login</Link></p>
    </div>
  );
}

export default ResetPassword;
