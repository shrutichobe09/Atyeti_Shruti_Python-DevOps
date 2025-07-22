from fastapi import FastAPI
from app.db.database import SessionLocal
from app.db.models import AlertLog

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "running"}

@app.get("/alerts")
def get_alerts():
    db = SessionLocal()
    alerts = db.query(AlertLog).order_by(AlertLog.timestamp.desc()).limit(10).all()
    return [{"message": a.message, "time": a.timestamp} for a in alerts]
