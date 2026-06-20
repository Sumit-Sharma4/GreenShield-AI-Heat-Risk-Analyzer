import HeatMap from "./HeatMap";
import { useState } from "react";
import {
  analyzeCity,
  getHotspots
} from "../services/api";

import AnalysisCard from "./AnalysisCard";
import HotspotDashboard from "./HotspotDashboard";
import LoadingSpinner from "./LoadingSpinner";
import AIChat from "./AIChat";

function CitySearch() {

  const [city, setCity] = useState("");
  const [result, setResult] = useState(null);
  const [hotspots, setHotspots] = useState([]);
  const [loading, setLoading] = useState(false);
  const [hotspotLoading, setHotspotLoading] = useState(false);

  const handleSearch = async () => {

    if (!city.trim()) {
      alert("Enter a city name");
      return;
    }

    try {

      setLoading(true);

      setResult(null);
      setHotspots([]);

      const cityData = await analyzeCity(city);

      setResult(cityData);

    } catch (error) {

      console.error(error);

      alert("Failed to analyze city");

    } finally {

      setLoading(false);

    }
  };

  // OUTSIDE handleSearch
  const handleHotspotAnalysis = async () => {

  try {

    setHotspotLoading(true);

    const hotspotData = await getHotspots(city);

    setHotspots(
      hotspotData.hotspots || []
    );

  } catch (error) {

    console.error(error);

    alert("Failed to analyze hotspots");

  } finally {

    setHotspotLoading(false);

  }
};
  return (

    <div>

      <input
        type="text"
        placeholder="Enter City Name"
        value={city}
        onChange={(e) =>
          setCity(e.target.value)
        }
      />

      <button onClick={handleSearch}>
        Analyze City
      </button>

      {loading && (
        <LoadingSpinner />
      )}

      {result && (

        <>

          {/* City Overview */}
          <AnalysisCard
            data={result}
          />

          {/* Interactive Heat Map */}
        <HeatMap
        center={result.coordinates}
        hotspots={hotspots}
        />

        <div
        style={{
        textAlign: "center",
        margin: "20px"
        }}
        >
       <button
  className="analysis-btn"
  onClick={handleHotspotAnalysis}
  disabled={hotspotLoading}
>
  {
    hotspotLoading
      ? "⏳ Analyzing Hotspots..."
      : "🔥 Generate Top 10 Hotspots"
  }
</button>
    {hotspotLoading && (

  <div
    style={{
      textAlign: "center",
      marginTop: "15px",
      fontWeight: "bold",
      color: "#e67e22"
    }}
  >
    🔥 Scanning localities...
    Please wait 20–60 seconds.
  </div>

)}
    </div>

      {hotspots.length > 0 && (

      <HotspotDashboard
      hotspots={hotspots}
      city={city}
      />

      )}
          {/* AI Assistant */}
          <AIChat
            city={city}
          />

        </>

      )}

    </div>

  );
}

export default CitySearch;