import React from "react";

const Header: React.FC = () => {
  const handleLogoClick = () => {
    window.location.reload();
  };

  return (
    <header className="header">
      <div className="logo-container" onClick={handleLogoClick} style={{ cursor: 'pointer' }}>
        <img src="/quantai_logo.png" alt="QuantAI Logo" className="logo" />
        <span className="company-name">QuantAI</span>
      </div>
      <div className="header-title">
        <h1>Car Finder</h1>
        <p>Your one-stop destination to find the best cars in New Zealand</p>
      </div>
    </header>
  );
};

export default Header;
