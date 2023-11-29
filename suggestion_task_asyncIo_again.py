import asyncio
import argparse
from requests import get
import json
import logging

# Add logger for the task
logging.basicConfig(filename="suggestion_task_asyncIo_again.log ", filemode="w", level=logging.INFO)
logger = logging.getLogger('my_logger')

# hit api
# create an async function
async def fetch_suggestions(target_keyword):
    api = get(f"http://suggestqueries.google.com/complete/search?client=firefox&q={target_keyword}")
    # we to show our data in json form
    jason_data = api.json()
    # now i want to separate keyword and suggetion only no need of extra data 
    keyword = jason_data[0]
    suggestions = jason_data[1]
    # checking miss spelled
    miss_spelled = None
    if keyword in jason_data[1]:
        miss_spelled = False
    elif len(keyword) <= 2:
        miss_spelled = False
    else:
        res = None
        for j in jason_data[1]:
            if res is None or len(j) < len(res):
                res = j
        if len(keyword) > len(res):
            miss_spelled = True
    # Now if miss spelled True then shorrtest suggestion is the correct keyword
    smallest_suggestion = None
    if miss_spelled:
            for k in jason_data[1]:
                 if smallest_suggestion is None or len(k) < len(keyword):
                      smallest_suggestion = k

    # Display Result in formate
    display = {
        "keyword": keyword,
        "suggestions": suggestions,
        "miss_spelled": miss_spelled,
        "correct_keyword": smallest_suggestion
    }
    
    return display

async def fetch_all_suggestions(keywords):
    display = await asyncio.gather(*[fetch_suggestions(keyword) for keyword in keywords])
    return display



# pass Argument using argparse
parser = argparse.ArgumentParser()
parser.add_argument('my_list', nargs='+')
args = parser.parse_args()
keywords = args.my_list

results = asyncio.run(fetch_all_suggestions(keywords))
results1 = json.dumps(results, indent=4)
logger.info(results1)
