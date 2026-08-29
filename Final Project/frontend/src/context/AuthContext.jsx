import { createContext, useContext, useEffect, useState } from "react";
import { apiFetch } from "../api";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  async function loadProfile() {
    if (!localStorage.getItem("access")) {
      setLoading(false);
      return;
    }
    const res = await apiFetch("/api/auth/profile/");
    if (res.ok) {
      setUser(res.data);
    } else {
      // token expired or invalid
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
    }
    setLoading(false);
  }

  useEffect(() => {
    loadProfile();
  }, []);

  async function login(email, password) {
    const res = await apiFetch("/api/auth/login/", {
      method: "POST",
      body: { email, password },
    });
    if (res.ok) {
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      await loadProfile();
    }
    return res;
  }

  function logout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
