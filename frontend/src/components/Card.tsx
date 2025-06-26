import React from "react";

const Card: React.FC<{ car: any }> = ({ car }) => {
  return (
    <div className="card">
      <img src={car.image} alt={car.title} />
      <div className="card-body">
        <h3>
          <span>{car.title}</span>
        </h3>
        <p>
          <strong>Price:</strong> <span>{car.price}</span>
        </p>
        <p>
          <strong>Odometer:</strong> <span>{car.odometer}</span>
        </p>
        <p>
          <strong>Fuel:</strong> <span>{car.fuel}</span>
        </p>
        <p>
          <strong>Consumption:</strong> <span>{car.consumption}</span>
        </p>
        <p>
          <strong>Source:</strong> <span>{car.source}</span>
        </p>
        <a href={car.link} target="_blank" rel="noopener noreferrer">
          View
        </a>
      </div>
    </div>
  );
};

export default Card;
