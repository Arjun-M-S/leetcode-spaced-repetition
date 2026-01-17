import json 
import time 
import random

def pick():
    try: 
        with open("solved_with_dates.json" , "r") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print("Database Does not Exist")
        return []
    
    data.sort(key= lambda x: x['last_solved_timestamp'])

    pool_size = max(10 , int(len(data)*0.2))
    print(pool_size)
    pool = data[:pool_size]

    print(f"picking from a pool of {pool_size} questions")

    picks = []
    hards = [q for q in pool if q['difficulty'] == 'HARD']
    mediums = [q for q in pool if q['difficulty'] == 'MEDIUM']
    easy = [q for q in pool if q['difficulty'] == 'EASY']


    first_pick = None
    if hards and random.random() > 0.5:
        first_pick = random.choice(hards)
    elif mediums:
        first_pick = random.choice(mediums)
    else: 
        first_pick = random.choice(easy)
    picks.append(first_pick)
    
    remaining_pool = [q for q in pool if q['id'] != first_pick['id']]
    if remaining_pool: 
        picks.append(random.choice(remaining_pool))

    return picks


if __name__ == "__main__":
    picks = pick()
    for q in picks: 
        print(f"{q['id']}:{q['title']}")