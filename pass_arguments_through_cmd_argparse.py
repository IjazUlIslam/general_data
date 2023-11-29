import argparse
from requests import get
parser = argparse.ArgumentParser()
parser.add_argument('my_list', nargs='+')
args = parser.parse_args()
keyword = args.my_list
for i in keyword:
    api = get(f"http://suggestqueries.google.com/complete/search?client=firefox&q={i}")
    data_in_json = api.json()
    print(data_in_json[1])
    print()