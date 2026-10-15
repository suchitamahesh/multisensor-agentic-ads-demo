from __future__ import annotations

import os
from typing import Dict, List

import requests
import streamlit as st

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Multisensor Anomaly Dashboard", layout="wide")


def fetch_overview() -> Dict[str, object]:
    try:
        resp = requests.get(f"{API_BASE_URL}/overview", timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except requests.RequestException:
        pass

    return {
        "status": "demo",
        "severity": "medium",
        "anomaly_count": 3,
        "likely_root_cause": "compressor_thermal_overload",
        "confidence": 0.86,
        "recommendations": [
            "Check thermal load.",
            "Inspect cooling loop.",
            "Review recent load spikes."
        ],
        "anomalies": ["temperature", "power_draw", "vibration"],
    }


st.title("Multisensor Anomaly Detection Dashboard")
st.caption("Software-only demo for anomaly detection, diagnosis, and decision support")

overview = fetch_overview()

col1, col2, col3 = st.columns(3)
col1.metric("Status", overview.get("status", "unknown").upper())
col2.metric("Severity", overview.get("severity", "medium").upper())
col3.metric("Anomaly Count", overview.get("anomaly_count", 0))

st.subheader("Likely Root Cause")
st.write(f"{overview.get('likely_root_cause', 'unknown')} (confidence: {overview.get('confidence', 0.0)})")

st.subheader("Recommendations")
for item in overview.get("recommendations", []):
    st.markdown(f"- {item}")

st.subheader("Detected Sensors")
for sensor in overview.get("anomalies", []):
    st.markdown(f"- {sensor}")

if st.button("Refresh"):
    st.rerun()
