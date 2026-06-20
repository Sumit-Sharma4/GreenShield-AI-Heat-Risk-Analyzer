from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.hotspot_csv import router as hotspot_csv_router
from app.routes.csv_report import router as csv_router
from app.routes.report import router as report_router
from app.routes.export import router as export_router
from app.routes.analyze import router as analyze_router
from app.routes.hotspots import router as hotspots_router
from app.routes.dashboard import router as dashboard_router

app = FastAPI(
    title="GreenShield AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(analyze_router)
app.include_router(hotspots_router)
app.include_router(dashboard_router)
app.include_router(export_router)
app.include_router(report_router)
app.include_router(csv_router)
app.include_router(hotspot_csv_router)

@app.get("/")
def home():
    return {
        "project": "GreenShield AI",
        "status": "Running"
    }