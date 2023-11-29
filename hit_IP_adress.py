from requests import get
api = get("http://suggestqueries.google.com/complete/search?client=firefox&q=laptop")
data_in_json = api.json()
print(data_in_json[0])