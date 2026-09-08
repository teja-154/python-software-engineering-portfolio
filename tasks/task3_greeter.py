import json, sys
terminal_values=sys.argv
try:
    with open("config.json","r") as file:
        data=json.load(file)
        if len(terminal_values)>1:
            user_name=terminal_values[1]
        else:
            user_name=data["default_name"]
        greet_style=data["greeting_style"]
except FileNotFoundError:
    user_name=data["default_name"]
    greet_style=data["greeting_style"]
print(f"Greetings, {user_name}. We wish you a productive engineering session." if greet_style=='formal' else f"Hey {user_name}! Ready to crush some code today? 🚀")