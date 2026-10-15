from __future__ import annotations

from typing import Dict, List

from app.diagnosis import diagnose_anomalies
from app.models import summarize_anomalies
from app.sensor_simulator import SensorSimulator


class DecisionSupportAgent:
    """Agentic triage layer for anomaly detection and recommendations."""

    def __init__(self, threshold: float = 3.0):
        self.threshold = threshold

    def triage(self, sensor_data: Dict[str, List[float]]) -> Dict[str, object]:
        summary = summarize_anomalies(sensor_data, threshold=self.threshold)
        diagnosis = diagnose_anomalies(summary)

        return {
            "status": diagnosis["status"],
            "severity": diagnosis["severity"],
            "anomaly_count": summary["anomaly_count"],
            "likely_root_cause": diagnosis["likely_root_cause"],
            "confidence": diagnosis["confidence"],
            "anomalies": summary["anomalies"],
            "recommendations": diagnosis["recommendations"],
            "sensor_summary": summary["sensors"],
        }

    def generate_demo_run(self) -> Dict[str, object]:
        data = SensorSimulator().generate()
        return self.triage(data)
