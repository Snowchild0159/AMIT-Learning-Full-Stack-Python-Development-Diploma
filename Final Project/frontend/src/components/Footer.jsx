function Footer() {
  return (
    <footer className="footer">
      <div className="footer-grid">
        <section>
          <h3>Contact</h3>
          <p className="footer-muted">Questions? Go ahead.</p>
          <p className="footer-muted">hello@mahally.com</p>
          <p className="footer-muted">01001234567</p>
        </section>
        <section>
          <h3>About</h3>
          <ul className="footer-list">
            <li>About Mahally</li>
            <li>Support</li>
            <li>Shipment</li>
            <li>Payment</li>
            <li>Returns</li>
          </ul>
        </section>
        <section>
          <h3>Store</h3>
          <ul className="footer-list">
            <li>Mahally — محلّي</li>
            <li>Egyptian local marketplace</li>
            <li>We accept</li>
            <li className="footer-muted">Cash on Delivery • Demo Card</li>
          </ul>
        </section>
      </div>
      <div className="footer-bottom">© {new Date().getFullYear()} Mahally</div>
    </footer>
  );
}

export default Footer;
