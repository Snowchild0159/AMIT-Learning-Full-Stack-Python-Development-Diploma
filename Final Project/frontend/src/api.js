export const host = "http://localhost:8000";

// small helper so every request attaches the JWT token automatically
export async function apiFetch(path, options = {}) {
  const token = localStorage.getItem("access");
  const headers = { ...(options.headers || {}) };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }
  if (options.body && !(options.body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
    options.body = JSON.stringify(options.body);
  }
  const response = await fetch(`${host}${path}`, { ...options, headers });
  let data = null;
  try {
    data = await response.json();
  } catch {
    data = null;
  }
  return { ok: response.ok, status: response.status, data };
}

// turns DRF error objects into one readable message
export function errorText(data) {
  if (!data) return "Something went wrong.";
  if (typeof data === "string") return data;
  if (data.detail) return data.detail;
  return Object.entries(data)
    .map(([field, msgs]) => `${field}: ${Array.isArray(msgs) ? msgs.join(" ") : msgs}`)
    .join(" | ");
}
