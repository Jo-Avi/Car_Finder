import React from 'react';
import './Loading.css';

const Loading: React.FC = () => {
  return (
    <div className="loading-container">
      <div className="car-loader">
        <div className="car-body">
          <div className="windshield"></div>
          <div className="front-fascia"></div>
          <div className="taillight"></div>
          <div className="headlight"></div>
          <div className="grille"></div>
          <div className="mirror-left"></div>
          <div className="mirror-right"></div>
          <div className="handle-left"></div>
          <div className="handle-right"></div>
          <div className="license-plate">ABC123</div>
          <div className="bumper-front"></div>
          <div className="bumper-rear"></div>
        </div>
        <div className="car-wheel-left"></div>
        <div className="car-wheel-right"></div>
        <div className="exhaust"></div>
        <div className="exhaust"></div>
        <div className="exhaust"></div>
      </div>
      <div className="road-line"></div>
      <p>Loading cars...</p>
    </div>
  );
};

export default Loading; 