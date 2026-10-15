# Multisensor Agentic Anomaly Detection, Diagnosis and Decision Support System

A software-only, end-to-end project for detecting anomalies across multiple sensor streams, diagnosing likely faults, and recommending actions using an agentic decision-support layer.

This project is designed to be runnable locally with minimal dependencies and to be extended into a real production system.

## Features

- Synthetic sensor stream generator for multiple sensor types
- Baseline anomaly detection with robust statistical methods
- Diagnosis logic for likely root cause and impacted systems
- Agentic triage workflow with recommendation generation
- FastAPI backend service for ingestion and analysis
- Streamlit dashboard for monitoring and operator decisions
- Docker Compose setup for running API and dashboard together
- CI-ready test suite

## Architecture

- Ingestion layer: simulated multisensor event data and API ingestion
- Detection layer: multi-sensor anomaly scoring and thresholding
- Diagnosis layer: attribution of anomalies to likely subsystem or sensor fault
- Decision support layer: agent that proposes actions with confidence and priority
- UX layer: dashboard for visualizing alerts and recommended actions

## Project Layout

```text
.
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── api.py
│   ├── config.py
│   ├── dashboard.py
│   ├── diagnosis.py
│   ├── main.py
│   ├── models.py
│   └── sensor_simulator.py
├── tests/
│   ├── test_agent.py
│   └── test_models.py
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
└── run_demo.py
```

## Quick Start

### 1. Create environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the API service

```bash
python -m uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Run the dashboard

```bash
streamlit run app/dashboard.py --server.port 8501
```

### 4. Or run everything with Docker Compose

```bash
docker compose up --build
```

Then open:
- API: http://localhost:8000/docs
- Dashboard: http://localhost:8501

## Demo Workflow

The project comes with a synthetic workload that simulates:

- temperature sensor drift
- pressure anomalies
- vibration spikes
- flow irregularities
- system-level status degradation

The agent evaluates all sensors and outputs a triage result such as:

```json
{
  "status": "warning",
  "severity": "high",
  "anomaly_count": 3,
  "likely_root_cause": "compressor_thermal_overload",
  "confidence": 0.88,
  "recommendations": [
    "Check compressor thermal load and cooling efficiency.",
    "Inspect vibration sensors for mechanical imbalance."
  ]
}
```

## Environment Variables

Copy `.env.example` to `.env` and adjust values as needed.

```bash
cp .env.example .env
```

## Testing

```bash
pytest -q
```

## Notes

This is a software-first demo intentionally built without hardware dependencies. It is ready to be extended into a production-grade system with real-time ingestion, model retraining, and enterprise decision support workflows.

## License

MIT
