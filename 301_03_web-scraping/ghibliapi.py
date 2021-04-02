import requests

response = requests.get("https://ghibliapi.herokuapp.com/films")
data = response.json()

longest = max([(int(f["running_time"]), f["release_date"], f["original_title"], f["title"]) for f in data])
print(longest)

# OUTPUT:
# (137, '2013', 'かぐや姫の物語', 'The Tale of the Princess Kaguya')
