

# 🧠 LeetCode Spaced Repetition Bot

A fully automated Python tool that syncs your LeetCode submission history and emails you two "forgotten" questions every day. It uses a **Weighted Spaced Repetition Algorithm** to prioritize questions you haven't solved in a long time, helping you retain patterns for technical interviews.

## 🚀 Features

* **Reverse Engineered API:** Syncs submission history directly from LeetCode's GraphQL endpoint (bypassing the lack of a public API).
* **Spaced Repetition Logic:**
    * **Time-Decay Sorting:** Prioritizes the oldest 20% of your solved questions.
    * **Difficulty Bias:** Intelligently attempts to force at least one "Medium" or "Hard" question per day to prevent stagnation.
* **Automated Emailer:** Sends a clean HTML daily digest with direct links to the problems.
* **Zero-Server Cost:** Runs on a local machine via Task Scheduler (or GitHub Actions).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Networking:** `requests` (Raw HTTP/1.1 with custom headers to mimic browser sessions)
* **Data:** JSON (Local persistence)
* **Automation:** SMTP (Email) & Windows Task Scheduler

## ⚙️ Setup & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/leetcode-spaced-repetition.git](https://github.com/YOUR_USERNAME/leetcode-spaced-repetition.git)
cd leetcode-spaced-repetition

```

### 2. Install Dependencies

```bash
pip install requests

```

### 3. Configure Secrets (Important!)

This project relies on a local secrets file that is **ignored by Git** for security.

1. Find the file `LEETCODE_SESSION_TEMPLATE.py`.
2. Rename it to `LEETCODE_SESSION.py`.
3. Open it and fill in your credentials:

```python
# LEETCODE_SESSION.py
LEETCODE_SESSION = "your_long_session_cookie_string"
x_csrftoken = "your_csrf_token"
EMAIL_PASSWORD = "your_16_char_google_app_password"

```

> **Note:** To get your LeetCode session, inspect your browser cookies (`LEETCODE_SESSION`) while logged into LeetCode. For Gmail, use an **App Password**, not your login password.

### 4. Run the Bot

You can run the script manually to test it:

```bash
python main.py

```

### 5. Automate (Windows)

1. Open **Task Scheduler**.
2. Create a Basic Task -> Trigger: "Daily at 9:00 AM".
3. Action: Start a Program -> Select your `python.exe`.
4. Arguments: `main.py`
5. **Start in:** `C:\Path\To\This\Folder` (Critical step!).

## 🤝 Contribution

Feel free to fork this repo and add features like "Streak Tracking" or "Notion Integration"!

## 📄 License

MIT

```
