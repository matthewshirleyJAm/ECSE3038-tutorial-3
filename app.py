from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def hottest(devices):
    best = devices[0]
    for device in devices:
        if device["temp"] > best["temp"]:
            best = device
    return best

@app.get("/devices")
def get_devices():
    return readings

@app.get("/devices/hottest")
def get_hottest():
    return hottest(readings)

@app.get("/devices/online")
def get_online():
    online_devices = []
    for device in readings:
        if device["online"]:
            online_devices.append(device)
    return online_devices