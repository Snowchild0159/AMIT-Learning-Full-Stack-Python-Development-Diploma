import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

// wraps pages that need a logged in user
function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  if (loading) return <p className="page-message">Loading...</p>;
  if (!user) return <Navigate to="/login" replace />;
  return children;
}

export default ProtectedRoute;
