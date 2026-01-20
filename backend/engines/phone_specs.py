import json
from pathlib import Path

# Load phones.json once (at import time)
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "phones.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    PHONES = json.load(f)


def get_phone_specs(phone_name: str) -> dict | None:
    return PHONES.get(phone_name)