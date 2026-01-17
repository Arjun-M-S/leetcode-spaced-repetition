import requests
import random 
from LEETCODE_SESSION_TEMPLATE import *
import json 
import time 


def fetch_solved_questions(): 
    url = "https://leetcode.com/graphql"

    leetcode_session = LEETCODE_SESSION
    CRSF_TOKEN = x_csrftoken

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={leetcode_session}; csrftoken={CRSF_TOKEN}",
        "x-csrftoken":CRSF_TOKEN, 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0",
        "Referer": "https://leetcode.com/problems/two-sum/"
    }


    query = """
    query userProgressQuestionList($filters: UserProgressQuestionListInput) {
      userProgressQuestionList(filters: $filters) {
        totalNum
        questions {
          frontendId
          title
          titleSlug
          difficulty
          lastSubmittedAt   
          numSubmitted
          questionStatus    
          topicTags {
            name
          }
        }
      }
    }
    """

    questions = []
    limit = 50 
    skip = 0
    total_scanned = 0

    while True: 
        payload = {
            "operationName": "userProgressQuestionList",
            "query":query, 
            "variables":{
                "filters":{
                    "limit":limit, 
                    "skip":skip
                }
            }

        }

        try: 
            response = requests.post(url , json=payload , headers=headers)

            if response.status_code != 200:
                print("Error 1")
                break 

            data = response.json()
            if "errors" in data:
                print(f"GraphQL Error: {data['errors']}")
                break

            data_node = data['data']['userProgressQuestionList']
            batch = data_node['questions']
            total_num = data_node['totalNum']

            if not batch: 
                break 

            for q in batch:
                if q['questionStatus'] == 'SOLVED':
                    questions.append({
                        "id": q['frontendId'],
                        "title": q['title'],
                        "slug": q['titleSlug'],
                        "difficulty": q['difficulty'],
                        "last_solved_timestamp": q['lastSubmittedAt'], 
                        "url": f"https://leetcode.com/problems/{q['titleSlug']}/"
                    })
            total_scanned += len(batch)
            print(f"   Scanned {total_scanned} items...")
            skip += limit
            if len(batch) < limit: 
                break 

            time.sleep(1)

        except Exception as e:
            print(f"Exception: {e}")
            break

    print(f"Found {len(questions)} accepted questions with timestamps.")
    return questions

if __name__ == "__main__":
    final_list = fetch_solved_questions()
    with open("solved_with_dates.json", "w") as f:
        json.dump(final_list, f, indent=4)