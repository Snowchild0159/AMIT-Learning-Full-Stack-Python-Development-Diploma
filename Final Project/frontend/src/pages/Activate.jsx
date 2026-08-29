import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { apiFetch } from "../api";

function Activate() {
  const { token } = useParams();
  const [message, setMessage] = useState("Activating your account...");
  const [ok, setOk] = useState(false);

  useEffect(() => {
    async function activate() {
      const res = await apiFetch(`/api/auth/activate/${token}/`);
      setMessage(res.data?.detail || "Something went wrong.");
      setOk(res.ok);
    }
    activate();
  }, [token]);

  return (
    <div className="page narrow">
      <h2>Account activation</h2>
      <p className={ok ? "success-banner" : "form-error"}>{message}</p>
      {ok && <Link to="/login">Go to login</Link>}
    </div>
  );
}

export default Activate;
