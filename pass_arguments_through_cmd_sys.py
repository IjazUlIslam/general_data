import sys
from requests import get

# get key word
arguments = sys.argv
keyword = arguments[1:]
for i in keyword:
    api = get(f"http://suggestqueries.google.com/complete/search?client=firefox&q={i}")
    data_in_json = api.json()
    print(data_in_json[1])
    print()