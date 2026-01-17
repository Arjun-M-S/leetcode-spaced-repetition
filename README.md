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
