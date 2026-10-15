from __future__ import annotations

import argparse

from app.agent import DecisionSupportAgent
from app.sensor_simulator import SensorSimulator


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the multisensor anomaly agent demo.")
    parser.add_argument("--threshold", type=float, default=3.0, help="Anomaly threshold")
    args = parser.parse_args()

    agent = DecisionSupportAgent(threshold=args.threshold)
    data = SensorSimulator().generate()
    result = agent.triage(data)
    print("=== Multisensor Agent Result ===")
    print(result)


if __name__ == "__main__":
    main()
