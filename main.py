from fetch_solved import fetch_solved_questions
from email_sender import send_daily_revision_email
from picker import pick
import json


if __name__ == "__main__":
    data = fetch_solved_questions()
    if not data: 
        print("No data received, aborting")
        exit()
    with open("solved_with_dates.json" , "w") as f: 
        json.dump(data, f)

    selected_questions = pick()
    
    send_daily_revision_email(selected_questions)