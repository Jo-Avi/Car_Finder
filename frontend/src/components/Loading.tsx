import React from 'react';
import './Loading.css';

const Loading: React.FC = () => {
  return (
    <div className="loading-container">
      <div className="car-loader">
        <div className="car-body"></div>
        <div className="car-wheel-left"></div>
        <div className="car-wheel-right"></div>
      </div>
      <div className="road-line"></div>
      <p>Loading cars...</p>
    </div>
  );
};

export default Loading; 