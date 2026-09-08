import json, sys
from pathlib import Path

terminal_values=sys.argv
config_path = Path(__file__).parent.parent / "config.json"
default_name = "Divya"
greet_style = "formal"

try:
    with open(config_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        user_name = terminal_values[1] if len(terminal_values) > 1 else data.get("default_name", default_name)
        greet_style = data.get("greeting_style", greet_style)
except (FileNotFoundError, json.JSONDecodeError):
    user_name = terminal_values[1] if len(terminal_values) > 1 else default_name

print(f"Greetings, {user_name}. We wish you a productive engineering session." if greet_style=='formal' else f"Hey {user_name}! Ready to crush some code today? 🚀")
