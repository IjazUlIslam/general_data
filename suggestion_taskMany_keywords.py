import argparse
from requests import get
parser = argparse.ArgumentParser()
parser.add_argument('my_list', nargs='+')
args = parser.parse_args()
keyword = args.my_list
for i in keyword:
    api = get(f"http://suggestqueries.google.com/complete/search?client=firefox&q={i}")
    data_in_json = api.json()
    dic_suggestions = {
        "keyword": data_in_json[0],
        "suggestions": data_in_json[1]
    }
    print(dic_suggestions)
    miss_spelled = None
    if keyword in data_in_json[1]:
        miss_spelled = False
    elif len(keyword) <= 2:
        miss_spelled = False
    else:
        res = None
        for i in data_in_json:
            if res is None or len(i) < len(res):
                res = i
        if len(keyword) > len(res):
            miss_spelled = True

dic_suggestions["missSpelled"] = miss_spelled
for key, value in dic_suggestions.items():
    print(f"{key} : {value}")
