# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.

import requests
from secrets import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT
from secrets import REDDIT_USERNAME, REDDIT_PASSWORD

client_auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_SECRET)
post_data = {"grant_type": "password", "username": REDDIT_USERNAME, "password": REDDIT_PASSWORD}
headers = {"User-Agent": REDDIT_USER_AGENT}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())
token = response.json()["access_token"]

headers = {"Authorization": f"bearer {token}", "User-Agent": REDDIT_USER_AGENT}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
print(response.json())