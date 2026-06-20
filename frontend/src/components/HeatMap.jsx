import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  Circle
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

function HeatMap({ center, hotspots = [] }) {

  if (!center) return null;

  return (
    <div className="card">

      <h2>🗺 Interactive Heat Map</h2>

      <MapContainer
        center={[center.lat, center.lon]}
        zoom={12}
        style={{
          height: "500px",
          width: "100%",
          borderRadius: "12px"
        }}
      >

        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {/* City Center Marker */}

        <Marker position={[center.lat, center.lon]}>
          <Popup>

            <strong>City Center</strong>

            <br />

            Latitude: {center.lat}

            <br />

            Longitude: {center.lon}

            <br /><br />

            <a
              href={`https://maps.google.com/?q=${center.lat},${center.lon}`}
              target="_blank"
              rel="noreferrer"
            >
              Open Google Maps
            </a>

          </Popup>
        </Marker>

        {/* 5 km Analysis Circle */}

        <Circle
          center={[center.lat, center.lon]}
          radius={10000}
          pathOptions={{
            color: "blue",
            fillColor: "blue",
            fillOpacity: 0.1
          }}
        />

        {/* Hotspot Markers */}

        {hotspots.map((item) => (

          <Marker
            key={item.rank}
            position={[item.lat, item.lon]}
          >
            <Popup>

              <strong>
                #{item.rank} {item.name}
              </strong>

              <br />

              Heat Score:
              {" "}
              {item.score.toFixed(2)}

              <br />

              Heat Index:
              {" "}
              {item.heat_index}

              <br />

              Risk:
              {" "}
              {item.risk}

              <br />

              Tree Cover:
              {" "}
              {item.landcover.tree_cover}%

              <br />

              Trees Needed:
              {" "}
              {item.trees_needed}

              <br /><br />

              <a
                href={item.google_maps}
                target="_blank"
                rel="noreferrer"
              >
                Open Google Maps
              </a>

            </Popup>
          </Marker>

        ))}

      </MapContainer>

      <p style={{ marginTop: "10px" }}>
        📍 Blue circle represents the 10 km city overview analysis area
        (≈ 314 km²).
      </p>

    </div>
  );
}

export default HeatMap;