#!/usr/bin/env python3

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

HOOK_DIR = Path(__file__).resolve().parent
REPO_ROOT = HOOK_DIR.parent
CONFIG_FILE = HOOK_DIR / "prompt_agent_action_tracker.json"


def load_config():
    try:
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Hook config not found: {CONFIG_FILE}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in hook config: {error}")


def parse_metadata(raw):
    if raw is None:
        return {}
    if isinstance(raw, dict):
        return raw
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw": raw}


def build_payload(args):
    payload = {
        "event": args.event,
        "agent": args.agent,
        "tool": args.tool,
        "prompt": args.prompt,
        "action": args.action,
        "metadata": parse_metadata(args.metadata),
    }
    return payload


def write_log(destination, record):
    target = Path(destination)
    if not target.is_absolute():
        target = REPO_ROOT / target
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def log_event(payload, config):
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "event": payload.get("event"),
        "agent": payload.get("agent"),
        "tool": payload.get("tool"),
        "prompt": payload.get("prompt"),
        "action": payload.get("action"),
        "metadata": payload.get("metadata", {}),
    }
    destination = config["action"].get("destination", ".github/hooks/prompt_agent_actions.log")
    write_log(destination, record)


def dispatch_event(payload):
    config = load_config()
    if payload["event"] not in config.get("events", []):
        raise SystemExit(f"Event '{payload['event']}' is not configured in {CONFIG_FILE}")

    action = config.get("action", {})
    if action.get("type") == "log":
        log_event(payload, config)
    else:
        raise SystemExit(f"Unsupported hook action type: {action.get('type')}")


def parse_stdin_payload():
    if sys.stdin.isatty():
        return None

    raw = sys.stdin.read()
    if not raw.strip():
        return None

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dispatch hook events based on hook config.")
    parser.add_argument("--event", help="Event name")
    parser.add_argument("--agent", help="Agent name", default=None)
    parser.add_argument("--tool", help="Tool name", default=None)
    parser.add_argument("--prompt", help="Prompt text", default=None)
    parser.add_argument("--action", help="Action name", default=None)
    parser.add_argument("--metadata", help="JSON metadata string", default=None)
    args = parser.parse_args()

    payload = None
    stdin_payload = parse_stdin_payload()
    if stdin_payload:
        payload = stdin_payload
    elif args.event:
        payload = build_payload(args)
    else:
        parser.print_help()
        raise SystemExit(1)

    dispatch_event(payload)
