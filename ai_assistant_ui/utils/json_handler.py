import json
import os

DATA_PATH = "ai_assistant_ui/data/assistant_data.json"

def load_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)

def update_user(username, details):
    data = load_data()
    data["users"][username] = details
    save_data(data)

def add_custom_object(object_name):
    data = load_data()
    if object_name not in data["custom_objects"]:
        data["custom_objects"].append(object_name)
        save_data(data)

def add_recognized_device(device_id):
    data = load_data()
    if device_id not in data["recognized_devices"]:
        data["recognized_devices"].append(device_id)
        save_data(data)
