import os
from slack_sdk.webhook import WebhookClient


f = open("diff.txt")
members = set()
for line in f.readlines():
    split = line.replace('"', '').split("/")
    if split[0] == "members":
        members.add(split[1])

f.close()

for member in members:
    url = os.environ.get("SLACK_WEBHOOK_URL")
    webhook = WebhookClient(url)
    response = webhook.send(text=f"{member}님이 문제를 푸셨습니다.")

    assert response.status_code == 200
    assert response.body == "ok"
