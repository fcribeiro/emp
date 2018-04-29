import json


def delete_app(appID):
    payload = {"id": appID, "name": "Songs Application", "state": "Stopped"}
    payload = json.dumps(payload)
    return json.loads(payload)
