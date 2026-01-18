from fetch_solved import *
from email_sender import *
from picker import *

if __name__ == "__main__":
    fetch_solved_questions()
    send_daily_revision_email(pick())