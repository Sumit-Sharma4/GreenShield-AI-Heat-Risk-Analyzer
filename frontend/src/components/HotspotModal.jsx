import LandcoverChart from "./LandcoverChart";
function HotspotModal({ hotspot, onClose }) {

  if (!hotspot) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">

        <button
          className="close-btn"
          onClick={onClose}
        >
          ✖
        </button>

        <h2>
          {hotspot.name} (1 km Radius Analysis)
        </h2>

        <p><b>🔥 Heat Score:</b> {hotspot.score.toFixed(2)}</p>
        <p><b>🌡 Heat Index:</b> {hotspot.heat_index}</p>
        <p><b>⚠ Risk:</b> {hotspot.risk}</p>

        <hr />

        <p><b>🌳 Tree Cover:</b> {hotspot.landcover.tree_cover}%</p>
        <p><b>🏢 Built-up:</b> {hotspot.landcover.built_up}%</p>
        <p><b>💧 Water:</b> {hotspot.landcover.water}%</p>
        <p><b>🌱 Grass:</b> {hotspot.landcover.grass}%</p>
        <p><b>🌾 Cropland:</b> {hotspot.landcover.cropland}%</p>
        <p><b>🌿 Shrub:</b> {hotspot.landcover.shrub}%</p>
        <LandcoverChart
         landcover={hotspot.landcover}
         />
        <hr />

        <p>
          <b>🌳 Trees Needed:</b> {hotspot.trees_needed}
        </p>

        <h3>🔥 Root Causes</h3>
        <ul>
          {hotspot.root_causes.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>

        <h3>🌳 Plantation Strategy</h3>
        <ul>
          {hotspot.plantation_strategy.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>

        <h3>📌 Recommendations</h3>
        <ul>
          {hotspot.recommendations.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>

        <a
          href={hotspot.google_maps}
          target="_blank"
          rel="noreferrer"
          className="map-btn"
        >
          Open Google Maps
        </a>

      </div>
    </div>
  );
}

export default HotspotModal;