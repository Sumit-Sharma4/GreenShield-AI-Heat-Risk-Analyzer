# 🌳 GreenShield AI Heat Risk Analyzer

## AI-Powered Urban Heat Risk Analysis and Climate Action Platform

GreenShield AI is an intelligent climate-tech platform that analyzes urban heat risk using satellite imagery, land-cover analysis, sustainability assessment, hotspot detection, and AI-powered recommendations.

The platform helps identify Urban Heat Island (UHI) effects, detect heat hotspots, estimate cooling potential, recommend tree plantation strategies, and provide actionable climate solutions for cities.

---

# 🚀 Features

# 🌳 GreenShield AI Heat Risk Analyzer

GreenShield AI is an AI-powered climate-tech platform that analyzes urban heat risk using satellite imagery and land-cover data. It helps identify heat hotspots, calculate sustainability scores, estimate cooling potential, and provide climate action recommendations for cities.

## 🚀 Features

* 🔥 Heat Risk Analysis
* 🌍 Sustainability Score & Grade
* 📊 Land Cover Analysis
* 🌳 Trees Needed Calculation
* 🌡 Cooling Potential Estimation
* 🔥 Root Cause Detection
* 🌱 Smart Plantation Strategy
* 🧠 Smart Climate Recommendations
* 🗺 Interactive Heat Map
* 🔥 Top 10 Hotspot Detection
* 🤖 Gemini AI Assistant
* 📄 PDF Report Generation

---

## 📸 Screenshots

### City Analysis Dashboard
![City Analysis](screenshots/city-analysis.png)

### Interactive Heat Map
![Heat Map](screenshots/heat-map.png)

### Hotspot Detection
![Hotspots](screenshots/hotspots.png)

### AI Assistant
![AI Assistant](screenshots/ai-assistant.png)

### Recommendations
![Recommendations](screenshots/recommendation.png)

---

# 🛠 Technology Stack

## Frontend

* React
* Vite
* React Leaflet
* Recharts
* Axios

---

## Backend

* FastAPI
* Python

---

## AI

* Google Gemini API

---

## Geospatial Technologies

* Google Earth Engine
* Dynamic World Dataset
* OpenStreetMap
* Nominatim Geocoder
* Overpass API

---

# 📂 Project Structure

```text
GreenShield-AI-Heat-Risk-Analyzer

├── backend
│
├── app
│   │
│   ├── routes
│   │   ├── analyze.py
│   │   ├── chat.py
│   │   ├── hotspots.py
│   │   ├── report.py
│   │   ├── export.py
│   │   ├── csv_report.py
│   │   └── hotspot_csv.py
│   │
│   ├── services
│   │   ├── geocoder.py
│   │   ├── landcover_analyzer.py
│   │   ├── heat_engine.py
│   │   ├── sustainability_score.py
│   │   ├── root_cause_engine.py
│   │   ├── recommendation_engine.py
│   │   ├── tree_calculator.py
│   │   ├── cooling_potential.py
│   │   ├── plantation_strategy.py
│   │   ├── hotspot_analyzer.py
│   │   ├── locality_fetcher.py
│   │   ├── locality_hotspot_analyzer.py
│   │   ├── smart_recommender.py
│   │   └── gemini_service.py
│   │
│   └── main.py
│
├── requirements.txt
│
├── frontend
│
├── src
│   │
│   ├── components
│   │   ├── CitySearch.jsx
│   │   ├── AnalysisCard.jsx
│   │   ├── HeatMap.jsx
│   │   ├── HotspotDashboard.jsx
│   │   ├── AIChat.jsx
│   │   ├── LandcoverChart.jsx
│   │   └── LoadingSpinner.jsx
│   │
│   ├── services
│   │   └── api.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── leafletFix.js
│
├── .gitignore
└── README.md
```

---

# ⚙ Installation

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# 🔑 Environment Variables

Create `.env` inside backend:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# 🔄 Workflow

1. Enter city name.
2. Generate city heat analysis.
3. View sustainability score.
4. Explore interactive heat map.
5. Generate Top 10 hotspots.
6. Review root causes.
7. Check trees needed.
8. View cooling potential.
9. Ask questions to AI Assistant.
10. Export PDF reports.

---

# 🎯 Future Enhancements

* City Comparison Dashboard
* Future Heat Prediction
* Climate Resilience Score
* Smart Tree Species Recommendation
* Real-Time Weather Integration
* Multi-City Ranking System
* Satellite Image Visualization
* Mobile Application

---

# 👨‍💻 Author

**Sumit Sharma**

B.Tech Computer Science Engineering Student

Developer of GreenShield AI Heat Risk Analyzer

Passionate about Artificial Intelligence, Sustainability, Climate Technology, and Software Development.
