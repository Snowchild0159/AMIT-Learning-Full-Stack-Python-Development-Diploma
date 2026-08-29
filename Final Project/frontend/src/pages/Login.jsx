import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { errorText } from "../api";

function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    const res = await login(email, password);
    if (res.ok) {
      navigate("/");
    } else if (res.status === 401) {
      setError("Wrong email/password, or the account is not activated yet.");
    } else {
      setError(errorText(res.data));
    }
  }

  return (
    <div className="page narrow">
      <h2>Login</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label>
          Email
          <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required />
        </label>
        <label>
          Password
          <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} required />
        </label>
        {error && <p className="form-error">{error}</p>}
        <button className="dark-button" type="submit">Login</button>
      </form>
      <p className="footer-muted">
        No account? <Link to="/register">Register</Link> •{" "}
        <Link to="/reset-password">Forgot password?</Link>
      </p>
    </div>
  );
}

export default Login;
