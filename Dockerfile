version: '3.9'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    command: python -m uvicorn app.api:app --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    environment:
      - API_HOST=0.0.0.0
      - API_PORT=8000
    restart: unless-stopped

  dashboard:
    build:
      context: .
      dockerfile: Dockerfile
    command: streamlit run app/dashboard.py --server.host 0.0.0.0 --server.port 8501
    ports:
      - "8501:8501"
    environment:
      - API_BASE_URL=http://api:8000
      - DASHBOARD_PORT=8501
    depends_on:
      - api
    restart: unless-stopped
