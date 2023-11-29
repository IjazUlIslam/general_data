import argparse
from requests import get
import logging
# import sys
# import json
import asyncio

# Add logger for the task
logging.basicConfig(filename="suggestion_task_asyncIo_Logging.log ", filemode="w", level=logging.INFO)
logger = logging.getLogger('my_logger')

# Fetch suggestions for each keywords
async def fetch_suggestions(target_keyword):
    api = get(f"http://suggestqueries.google.com/complete/search?client=firefox&q={target_keyword}")
    data_in_json = api.json()

    keyword = data_in_json[0]
    suggestions = data_in_json[1]

    # Checking if keyword is misspelled or not
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
    smallest_suggestion = None
    if miss_spelled:
        for j in data_in_json[1]:
            if smallest_suggestion is None or len(j) < len(keyword):
                smallest_suggestion = j

    # Formatting results
    result = {
        "keyword": keyword,
        "suggestions": suggestions,
        "misspelled": miss_spelled,
        "correct_keyword": smallest_suggestion
    }
    # result = json.dumps(result, indent=4)
    # logger.info(result)
    return result

async def fetch_all_suggestions(keywords):
    result = await asyncio.gather(*[fetch_suggestions(keyword) for keyword in keywords])
    return result

# Get arguments passed through command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('my_list', nargs='+')
    args = parser.parse_args()
    keywords = args.my_list

    results = asyncio.run(fetch_all_suggestions(keywords))
    print(results)
