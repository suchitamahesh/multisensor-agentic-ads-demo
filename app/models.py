from __future__ import annotations

import math
import random
from typing import Dict, List


class SensorSimulator:
    """Create synthetic multisensor telemetry with injected anomalies."""

    def __init__(self, num_points: int = 240, seed: int = 42):
        self.num_points = num_points
        self.seed = seed
        random.seed(seed)

    def _generate_baseline(self, idx: int, offset: float = 0.0) -> float:
        base = 50 + math.sin(idx / 18) * 8 + offset
        noise = random.uniform(-1.5, 1.5)
        return base + noise

    def generate(self) -> Dict[str, List[float]]:
        data: Dict[str, List[float]] = {
            "temperature": [],
            "pressure": [],
            "vibration": [],
            "flow_rate": [],
            "power_draw": [],
        }

        for idx in range(self.num_points):
            data["temperature"].append(self._generate_baseline(idx, 2.0))
            data["pressure"].append(self._generate_baseline(idx + 7, 10.0))
            data["vibration"].append(self._generate_baseline(idx + 13, 0.8))
            data["flow_rate"].append(self._generate_baseline(idx + 4, 6.0))
            data["power_draw"].append(self._generate_baseline(idx + 18, 12.0))

        anomaly_points = {
            "temperature": [80, 93, 110],
            "pressure": [120, 130, 140],
            "vibration": [90, 96, 109],
            "flow_rate": [72, 86, 95],
            "power_draw": [98, 104, 112],
        }

        for sensor_name, points in anomaly_points.items():
            for idx in points:
                if idx < self.num_points:
                    if sensor_name == "temperature":
                        data[sensor_name][idx] += 12
                    elif sensor_name == "pressure":
                        data[sensor_name][idx] += 20
                    elif sensor_name == "vibration":
                        data[sensor_name][idx] += 15
                    elif sensor_name == "flow_rate":
                        data[sensor_name][idx] -= 18
                    elif sensor_name == "power_draw":
                        data[sensor_name][idx] += 18

        return data
