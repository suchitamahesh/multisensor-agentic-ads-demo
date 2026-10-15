from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import numpy as np
from sklearn.ensemble import IsolationForest


@dataclass
class SensorAnomalyResult:
    sensor: str
    score: float
    z_score: float
    is_anomalous: bool
    mean: float
    std: float


class MultiSensorDetector:
    """Baseline detector using z-score and isolation forest score."""

    def __init__(self, threshold: float = 3.0):
        self.threshold = threshold

    def _zscore(self, series: List[float]) -> float:
        arr = np.asarray(series, dtype=float)
        mean = float(arr.mean())
        std = float(arr.std(ddof=0))
        if std == 0:
            return 0.0
        return float(abs((arr[-1] - mean) / std))

    def detect(self, sensor_data: Dict[str, List[float]]) -> Dict[str, SensorAnomalyResult]:
        results: Dict[str, SensorAnomalyResult] = {}
        for sensor_name, values in sensor_data.items():
            arr = np.asarray(values, dtype=float)
            mean = float(arr.mean())
            std = float(arr.std(ddof=0))
            z_value = 0.0 if std == 0 else float(abs((arr[-1] - mean) / std))
            model = IsolationForest(contamination=0.08, random_state=7)
            model.fit(arr.reshape(-1, 1))
            raw_score = model.decision_function(arr.reshape(-1, 1))
            latest_score = float(raw_score[-1])
            is_anomalous = z_value >= self.threshold or latest_score < -0.2
            results[sensor_name] = SensorAnomalyResult(
                sensor=sensor_name,
                score=float(abs(latest_score)),
                z_score=z_value,
                is_anomalous=is_anomalous,
                mean=mean,
                std=std,
            )
        return results


def summarize_anomalies(sensor_data: Dict[str, List[float]], threshold: float = 3.0) -> Dict[str, object]:
    detector = MultiSensorDetector(threshold=threshold)
    results = detector.detect(sensor_data)
    anomalies = {name: result for name, result in results.items() if result.is_anomalous}
    return {
        "total_sensors": len(sensor_data),
        "anomaly_count": len(anomalies),
        "sensors": {name: {
            "score": round(result.score, 4),
            "z_score": round(result.z_score, 4),
            "is_anomalous": result.is_anomalous,
        } for name, result in results.items()},
        "anomalies": list(anomalies.keys()),
    }
