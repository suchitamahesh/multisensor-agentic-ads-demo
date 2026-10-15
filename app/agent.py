from __future__ import annotations

from typing import Dict, List


def diagnose_anomalies(sensor_summary: Dict[str, object]) -> Dict[str, object]:
    sensors = sensor_summary.get("sensors", {})
    anomaly_keys = sensor_summary.get("anomalies", [])
    if not anomaly_keys:
        return {
            "status": "healthy",
            "severity": "low",
            "likely_root_cause": "normal_operation",
            "confidence": 0.95,
            "explanation": "No sensor anomalies detected above threshold.",
            "recommendations": ["Continue normal monitoring."],
        }

    sensor_scores = {}
    for sensor_name, metrics in sensors.items():
        if sensor_name in anomaly_keys:
            sensor_scores[sensor_name] = metrics.get("score", 0.0)

    strongest_sensor = max(sensor_scores, key=sensor_scores.get, default="temperature")

    if strongest_sensor in {"temperature", "power_draw"}:
        root_cause = "compressor_thermal_overload"
        recommendation = "Inspect cooling loop and compressor thermal load."
    elif strongest_sensor == "vibration":
        root_cause = "mechanical_imbalance_or_bearing_issue"
        recommendation = "Inspect bearings, couplings, and mechanical alignment."
    elif strongest_sensor == "pressure":
        root_cause = "fluid_flow_restriction_or_valve_issue"
        recommendation = "Check valve positions and pressure regulation components."
    elif strongest_sensor == "flow_rate":
        root_cause = "pump_or_line_restriction"
        recommendation = "Inspect pump performance and line restrictions."
    else:
        root_cause = "unknown_system_fault"
        recommendation = "Review sensor history and trigger manual inspection."

    confidence = min(0.99, 0.65 + (len(anomaly_keys) * 0.08))

    return {
        "status": "warning",
        "severity": "high" if len(anomaly_keys) >= 2 else "medium",
        "likely_root_cause": root_cause,
        "confidence": round(confidence, 2),
        " strongest_sensor": strongest_sensor,
        "explanation": f"The anomaly pattern is strongest in {strongest_sensor}, which is consistent with a likely subsystem fault.",
        "recommendations": [
            recommendation,
            "Cross-check sensor logs with maintenance history.",
            "Escalate to engineering review if pattern persists.",
        ],
    }

