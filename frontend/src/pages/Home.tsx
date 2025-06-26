import React, { useState, useEffect } from "react";
import Header from "../components/Header.tsx";
import Footer from "../components/Footer.tsx";
import Card from "../components/Card.tsx";
import Loading from "../components/Loading.tsx";
import "../index.css";
import "../components/Filters.css";

const Home: React.FC = () => {
  const [query, setQuery] = useState("");
  const [cars, setCars] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [fuelType, setFuelType] = useState<string>("");
  const [priceSort, setPriceSort] = useState<string>("");
  const [consumptionSort, setConsumptionSort] = useState<string>("");
  const [filteredCars, setFilteredCars] = useState<any[]>([]);

  const handleSearch = async () => {
    setLoading(true);
    const res = await fetch(`http://localhost:5000/search?q=${query}`);
    const data = await res.json();
    setCars(data);
    setLoading(false);
  };

  useEffect(() => {
    let result = [...cars];

    if (fuelType) {
      result = result.filter(
        (car) => car.fuel.toLowerCase() === fuelType.toLowerCase()
      );
    }

    if (priceSort) {
      result.sort((a, b) => {
        const priceA = parseFloat(a.price.replace(/[^0-9.-]+/g, ""));
        const priceB = parseFloat(b.price.replace(/[^0-9.-]+/g, ""));
        return priceSort === "asc" ? priceA - priceB : priceB - priceA;
      });
    }

    if (consumptionSort) {
      result.sort((a, b) => {
        const consumptionA = parseFloat(a.consumption);
        const consumptionB = parseFloat(b.consumption);
        return consumptionSort === "asc"
          ? consumptionA - consumptionB
          : consumptionB - consumptionA;
      });
    }

    setFilteredCars(result);
  }, [cars, fuelType, priceSort, consumptionSort]);

  return (
    <div className="app-container">
      <Header />
      <main className="main-content">
        <div className="search-section">
          <input
            type="text"
            placeholder="Search for cars (e.g., Toyota, Nissan...)"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button onClick={handleSearch}>Search</button>
        </div>
        {cars.length > 0 && (
          <div className="filters-section">
            <div className="filter-group">
              <label htmlFor="price-sort">Sort by Price:</label>
              <select
                id="price-sort"
                value={priceSort}
                onChange={(e) => setPriceSort(e.target.value)}
              >
                <option value="">None</option>
                <option value="asc">Ascending</option>
                <option value="desc">Descending</option>
              </select>
            </div>
            <div className="filter-group">
              <label htmlFor="fuel-type">Fuel Type:</label>
              <select
                id="fuel-type"
                value={fuelType}
                onChange={(e) => setFuelType(e.target.value)}
              >
                <option value="">All</option>
                <option value="petrol">Petrol</option>
                <option value="diesel">Diesel</option>
                <option value="electric">Electric</option>
                <option value="hybrid">Hybrid</option>
              </select>
            </div>
            <div className="filter-group">
              <label htmlFor="consumption-sort">Sort by Consumption:</label>
              <select
                id="consumption-sort"
                value={consumptionSort}
                onChange={(e) => setConsumptionSort(e.target.value)}
              >
                <option value="">None</option>
                <option value="asc">Ascending</option>
                <option value="desc">Descending</option>
              </select>
            </div>
          </div>
        )}
        {loading ? (
          <Loading />
        ) : (
          <div className="grid-container">
            {filteredCars.map((car, index) => (
              <Card key={index} car={car} />
            ))}
          </div>
        )}
      </main>
      <Footer />
    </div>
  );
};

export default Home;
