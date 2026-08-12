#!/usr/bin/env python3

import json
from datetime import datetime
from pathlib import Path
import sys

LOG_FILE = Path(__file__).with_name("prompt_agent_actions.log")


def log_event(event_data):
    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": event_data.get("event"),
        "agent": event_data.get("agent"),
        "tool": event_data.get("tool"),
        "prompt": event_data.get("prompt"),
        "action": event_data.get("action"),
        "metadata": event_data.get("metadata", {})
    }
    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        payload = {"event": "invalid_payload", "metadata": {"raw_input": sys.stdin.read()}}
    log_event(payload)
