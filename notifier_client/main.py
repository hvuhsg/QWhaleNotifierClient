import requests
from json import dumps

NOTIFIER_URL = "https://notifier.qwhale.ml"


class NotifierClient:
    def __init__(self, app_token: str):
        self.app_token = app_token

    def send_notification(self, user_token: str, title: str, body: str, url: str, data: dict) -> bool:
        data = dumps(data)
        response = requests.put(
            NOTIFIER_URL + f"/notifications/{user_token}?app_token={self.app_token}&title={title}&message={body}&url={url}",
            data=data
        )
        print(response.content)
        try:
            json = response.json()
            return "message" in json and json["message"] == "ok"
        except Exception:
            return False
