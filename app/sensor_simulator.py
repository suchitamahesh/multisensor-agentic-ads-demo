from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    dashboard_host: str = os.getenv("DASHBOARD_HOST", "0.0.0.0")
    dashboard_port: int = int(os.getenv("DASHBOARD_PORT", "8501"))
    model_threshold: float = float(os.getenv("MODEL_THRESHOLD", "3.0"))
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    api_base_url: str = os.getenv("API_BASE_URL", "http://localhost:8000")


settings = Settings()
