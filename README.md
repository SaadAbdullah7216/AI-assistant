# 🤖 AI Chatbot — Powered by OpenAI

A professional, modular ChatGPT-style chatbot built in Python. It maintains full conversation memory so the AI remembers everything you've discussed in the session.

---

## 📁 Project Structure

```
AI-Chatbot/
│
├── app.py            ← Main entry point, runs the chat loop
├── chatbot.py        ← Handles OpenAI API calls
├── memory.py         ← Manages conversation history (the "brain")
├── config.py         ← Loads API key & settings
├── requirements.txt  ← Python dependencies
├── .env              ← Secret API key (never share or commit!)
└── .gitignore        ← Prevents .env from being uploaded to GitHub
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the chatbot
```bash
python app.py
```

---

## 💬 Chat Commands

| Command   | Action                          |
|-----------|---------------------------------|
| `quit`    | Exit the chatbot                |
| `exit`    | Exit the chatbot                |
| `clear`   | Reset conversation memory       |
| `history` | Print full conversation history |

---

## 🧠 How Memory Works

Every message (user + assistant) is stored in a Python list called `history[]`.

On **every** API call, the **full history** is sent to OpenAI — this is why the bot remembers your name, past questions, and context. This is exactly how ChatGPT works.

```
history = [
  {"role": "system",    "content": "You are a helpful assistant..."},
  {"role": "user",      "content": "Hi, my name is Saad"},
  {"role": "assistant", "content": "Hello Saad! How can I help?"},
  {"role": "user",      "content": "What is my name?"},   ← new message
]
```

---

## ⚙️ Configuration

Edit `config.py` to change:
- `MODEL_NAME` — switch between `gpt-3.5-turbo` and `gpt-4`
- `SYSTEM_PROMPT` — change the bot's personality
- `BOT_NAME` / `USER_NAME` — display names

---

## 🔒 Security

- Your API key lives only in `.env`
- `.env` is listed in `.gitignore` — it will **never** be pushed to GitHub
- Never share your `.env` file with anyone
