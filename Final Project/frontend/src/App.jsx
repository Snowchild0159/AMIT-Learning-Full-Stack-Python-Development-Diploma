import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import { CartProvider } from "./context/CartContext";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";
import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./pages/Home";
import ProductDetails from "./pages/ProductDetails";
import Cart from "./pages/Cart";
import Checkout from "./pages/Checkout";
import Orders from "./pages/Orders";
import OrderDetails from "./pages/OrderDetails";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Activate from "./pages/Activate";
import ResetPassword from "./pages/ResetPassword";
import Profile from "./pages/Profile";
import SellerDashboard from "./pages/SellerDashboard";
import ProductForm from "./pages/ProductForm";

function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <AuthProvider>
      <CartProvider>
        <BrowserRouter>
          <Navbar onBurgerClick={() => setSidebarOpen(!sidebarOpen)} />
          <div className="layout">
            <Sidebar open={sidebarOpen} onClose={() => setSidebarOpen(false)} />
            <main className="main">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/product/:id" element={<ProductDetails />} />
                <Route path="/cart" element={<Cart />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/activate/:token" element={<Activate />} />
                <Route path="/reset-password" element={<ResetPassword />} />
                <Route path="/reset-password/:token" element={<ResetPassword />} />
                <Route path="/checkout" element={<ProtectedRoute><Checkout /></ProtectedRoute>} />
                <Route path="/orders" element={<ProtectedRoute><Orders /></ProtectedRoute>} />
                <Route path="/orders/:id" element={<ProtectedRoute><OrderDetails /></ProtectedRoute>} />
                <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
                <Route path="/seller" element={<ProtectedRoute><SellerDashboard /></ProtectedRoute>} />
                <Route path="/seller/new" element={<ProtectedRoute><ProductForm /></ProtectedRoute>} />
                <Route path="/seller/edit/:id" element={<ProtectedRoute><ProductForm /></ProtectedRoute>} />
              </Routes>
              <Footer />
            </main>
          </div>
        </BrowserRouter>
      </CartProvider>
    </AuthProvider>
  );
}

export default App;
