import LandcoverChart from "./LandcoverChart";

function AnalysisCard({ data }) {

  if (!data) return null;

  return (
    <div className="card">

      <h2>{data.city}</h2>

      <p>
        <strong>🔥 Heat Risk:</strong>{" "}
        {data.heat_risk}
      </p>

      <p>
        <strong>📈 Heat Score:</strong>{" "}
        {data.heat_score ?? "N/A"}
      </p>

      <p>
        <strong>🌍 Sustainability Score:</strong>{" "}
        {data.sustainability?.score ?? "N/A"}/100
      </p>

      <p>
        <strong>🏆 Grade:</strong>{" "}
        {data.sustainability?.grade ?? "N/A"}
      </p>

      <p>
        <strong>🌳 Tree Cover:</strong>{" "}
        {data.landcover?.tree_cover ?? 0}%
      </p>

      <p>
        <strong>🏢 Built Up:</strong>{" "}
        {data.landcover?.built_up ?? 0}%
      </p>

      <p>
        <strong>💧 Water:</strong>{" "}
        {data.landcover?.water ?? 0}%
      </p>

      <p>
        <strong>🌱 Grass:</strong>{" "}
        {data.landcover?.grass ?? 0}%
      </p>

      <p>
        <strong>🌾 Cropland:</strong>{" "}
        {data.landcover?.cropland ?? 0}%
      </p>

      <p>
        <strong>🌿 Shrub:</strong>{" "}
        {data.landcover?.shrub ?? 0}%
      </p>

      {data.landcover && (
        <LandcoverChart
          landcover={data.landcover}
        />
      )}

      <p>
        <strong>📍 Area Covered:</strong>{" "}
        {data.landcover?.radius_km
          ? `${data.landcover.radius_km} km Radius`
          : "5 km Radius"}
      </p>

      <p>
        <strong>🌳 Trees Needed:</strong>{" "}
        {data.trees_needed ?? "N/A"}
      </p>

      <p>
        <strong>🌡 Estimated Cooling:</strong>{" "}
        {data.cooling_potential ?? "N/A"}
      </p>

      {data.google_maps && (
  <>
    <br />

    <a
      href={data.google_maps}
      target="_blank"
      rel="noreferrer"
      className="map-btn"
    >
      Open Google Maps
    </a>

    <br /><br />

    <a
      href={`http://127.0.0.1:8000/report/${data.city}`}
      target="_blank"
      rel="noreferrer"
      className="map-btn"
    >
      📄 Download PDF Report
    </a>
  </>
    )}
      

      {data.root_causes?.length > 0 && (
        <>
          <h3>🔥 Root Causes</h3>

          <ul>
            {data.root_causes.map((cause, index) => (
              <li key={index}>
                {cause}
              </li>
            ))}
          </ul>
        </>
      )}

      {data.plantation_strategy?.length > 0 && (
        <>
          <h3>🌱 Plantation Strategy</h3>

          <ul>
            {data.plantation_strategy.map((item, index) => (
              <li key={index}>
                {item}
              </li>
            ))}
          </ul>
        </>
      )}

      {data.recommendations?.length > 0 && (
        <>
          <h3>🌳 Recommendations</h3>

          <ul>
            {data.recommendations.map((item, index) => (
              <li key={index}>
                {item}
              </li>
            ))}
          </ul>
        </>
      )}

    </div>
  );
}

export default AnalysisCard;