import { useState } from "react";
import HotspotModal from "./HotspotModal";

function HotspotDashboard({
  hotspots,
  city
  }) {

  const [selectedHotspot, setSelectedHotspot] = useState(null);
  const exportHotspotsCSV = (city) => {

  window.open(
    `http://127.0.0.1:8000/hotspot-csv/${city}`,
    "_blank"
  );

  };

  if (!hotspots || hotspots.length === 0) {
    return null;
  }

  return (
    <div className="card">

      <h2>🔥 Top 10 Heat Hotspots</h2>

      <p>
        Total Hotspots: <strong>{hotspots.length}</strong>
      </p>

      <table>
        <thead>
          <tr>
            <th>Rank</th>
            <th>Locality</th>
            <th>Heat Score</th>
            <th>Heat Index</th>
            <th>Risk</th>
            <th>Tree Cover</th>
            <th>Trees Needed</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>

          {hotspots.map((item) => (

            <tr key={item.rank}>

              <td>
                #{item.rank}
              </td>

              <td>
                {item.name}
              </td>

              <td>
                {item.score.toFixed(2)}
              </td>

              <td>
                {item.heat_index}
              </td>

              <td>
                {item.risk}
              </td>

              <td>
                {item.landcover.tree_cover}%
              </td>

              <td>
                🌳 {item.trees_needed}
              </td>

              <td>

  <div
    style={{
      display: "flex",
      flexDirection: "column",
      gap: "10px",
      alignItems: "center"
    }}
  >

    <a
      href={item.google_maps}
      target="_blank"
      rel="noreferrer"
      className="map-btn"
    >
      Map
    </a>

    <button
      className="analysis-btn"
      onClick={() => setSelectedHotspot(item)}
    >
      1 km Analysis
    </button>

    <a
      href={
        `http://127.0.0.1:8000/hotspot-csv?` +
        `name=${encodeURIComponent(item.name)}` +
        `&score=${item.score}` +
        `&heat_index=${item.heat_index}` +
        `&risk=${encodeURIComponent(item.risk)}` +
        `&tree_cover=${item.landcover.tree_cover}` +
        `&built_up=${item.landcover.built_up}` +
        `&water=${item.landcover.water}` +
        `&grass=${item.landcover.grass}` +
        `&cropland=${item.landcover.cropland}` +
        `&shrub=${item.landcover.shrub}` +
        `&trees_needed=${item.trees_needed}`
      }
      target="_blank"
      rel="noreferrer"
      className="analysis-btn"
    >
      Download CSV
    </a>

  </div>

</td>
            </tr>

          ))}

        </tbody>
      </table>

      <HotspotModal
        hotspot={selectedHotspot}
        onClose={() => setSelectedHotspot(null)}
      />

    </div>
  );
}

export default HotspotDashboard;