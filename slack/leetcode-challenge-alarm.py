import os
from slack_sdk.webhook import WebhookClient

url = os.environ.get("SLACK_WEBHOOK_URL")
webhook = WebhookClient(url)
response = webhook.send(text="LeetCode에서 새로운 챌린지 문제가 출제되었습니다. - https://leetcode.com")

assert response.status_code == 200
assert response.body == "ok"
