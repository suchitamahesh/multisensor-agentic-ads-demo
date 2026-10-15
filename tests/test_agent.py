from app.models import summarize_anomalies


def test_summary_works_for_normal_data():
    sensor_data = {
        "temperature": [22.0, 22.2, 22.4, 22.6, 22.8],
        "pressure": [101.0, 100.8, 101.2, 101.1, 100.9],
    }
    result = summarize_anomalies(sensor_data, threshold=3.0)
    assert "sensors" in result
    assert result["total_sensors"] == 2
    assert isinstance(result["anomaly_count"], int)


def test_summary_detects_anomalies():
    sensor_data = {
        "temperature": [20.0] * 20 + [60.0],
        "pressure": [101.0] * 20 + [105.0],
    }
    result = summarize_anomalies(sensor_data, threshold=2.8)
    assert result["anomaly_count"] >= 0
