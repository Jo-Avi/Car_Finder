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
  const [error, setError] = useState<string>("");
  const [fuelType, setFuelType] = useState<string>("");
  const [priceSort, setPriceSort] = useState<string>("");
  const [consumptionSort, setConsumptionSort] = useState<string>("");
  const [filteredCars, setFilteredCars] = useState<any[]>([]);

  const handleSearch = async () => {
    if (!query.trim()) {
      setError("Please enter a search term");
      return;
    }

    setLoading(true);
    setError("");
    setCars([]); // Clear previous results

    try {
      const res = await fetch(`https://car-scraping-6sl5.onrender.com/search?q=${encodeURIComponent(query)}`);
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      const data = await res.json();
      // Defensive: always set to array or empty array
      let results: any[] = [];
      if (Array.isArray(data.results)) {
        results = data.results;
      } else if (Array.isArray(data)) {
        results = data;
      } else {
        // If data is not an array and not an object with results, log it
        console.error("Unexpected API response format:", data);
      }
      setCars(results);
      if (results.length === 0) {
        setError("No cars found for your search. Try a different search term.");
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to search for cars. Please try again.");
      setCars([]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  useEffect(() => {
    let result = Array.isArray(cars) ? [...cars] : [];
    if (fuelType) {
      result = result.filter(
        (car) => car.fuel && car.fuel.toLowerCase() === fuelType.toLowerCase()
      );
    }
    if (priceSort) {
      result.sort((a, b) => {
        const priceA = parseFloat(a.price?.replace(/[^0-9.-]+/g, "") || "0");
        const priceB = parseFloat(b.price?.replace(/[^0-9.-]+/g, "") || "0");
        return priceSort === "asc" ? priceA - priceB : priceB - priceA;
      });
    }
    if (consumptionSort) {
      result.sort((a, b) => {
        const consumptionA = parseFloat(a.consumption || "0");
        const consumptionB = parseFloat(b.consumption || "0");
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
            onKeyPress={handleKeyPress}
          />
          <button onClick={handleSearch} disabled={loading}>
            {loading ? "Searching..." : "Search"}
          </button>
        </div>
        {error && (
          <div className="error-message" style={{
            color: 'red',
            textAlign: 'center',
            margin: '20px 0',
            padding: '10px',
            backgroundColor: '#ffe6e6',
            borderRadius: '5px'
          }}>
            {error}
          </div>
        )}
        {Array.isArray(cars) && cars.length > 0 && (
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
            {Array.isArray(filteredCars) && filteredCars.length > 0 ? (
              filteredCars.map((car, index) => (
                <Card key={index} car={car} />
              ))
            ) : Array.isArray(cars) && cars.length > 0 ? (
              <div style={{ 
                gridColumn: '1 / -1', 
                textAlign: 'center', 
                padding: '2rem',
                color: 'white'
              }}>
                No cars match your current filters. Try adjusting your filter settings.
              </div>
            ) : null}
          </div>
        )}
      </main>
      <Footer />
    </div>
  );
};

export default Home;
