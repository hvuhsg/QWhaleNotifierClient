# NotifierClient

### install
```shell script
$> pip install NotifierClient
```

### Use example
```python
from notifier_client import NotifierClient

app_token = "<Token>"
client = NotifierClient(app_token)
res = client.send_notification(
    user_token="<USER_TOKEN>",
    title="My first notification",
    body="message body",
    url="https://qwhale.com", # optional
    data={"Extra": "data"} # optional {string: string}
)
print(res) # -> {"message": "ok"} or {"message": "Invalid Token."}
```
