from __future__ import annotations

from typing import Dict, List

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.agent import DecisionSupportAgent
from app.sensor_simulator import SensorSimulator

app = FastAPI(title="Multisensor Decision Support API")
agent = DecisionSupportAgent()


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.get("/overview")
def overview() -> Dict[str, object]:
    demo = agent.generate_demo_run()
    return demo


@app.post("/simulate")
def simulate() -> Dict[str, object]:
    data = SensorSimulator().generate()
    result = agent.triage(data)
    return result


@app.get("/")
def root() -> Dict[str, str]:
    return {"message": "Multisensor anomaly detection API is running."}


@app.exception_handler(404)
def not_found_handler(_, __):
    return JSONResponse(status_code=404, content={"detail": "Not found."})
