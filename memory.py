from config import SYSTEM_PROMPT

# ── Conversation History ───────────────────────────────────────
# This list is the "brain" of the chatbot.
# Every message (user + assistant) is stored here.
# The full history is sent to the API on every call so GPT remembers.

history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def add_user_message(message: str):
    """Append a user message to the conversation history."""
    history.append({
        "role": "user",
        "content": message
    })


def add_assistant_message(message: str):
    """Append the assistant's reply to the conversation history."""
    history.append({
        "role": "assistant",
        "content": message
    })


def get_history() -> list:
    """Return the full conversation history."""
    return history


def clear_history():
    """Reset the conversation (keeps the system prompt)."""
    global history
    history = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
    print("\n🔄  Conversation cleared. Starting fresh!\n")


def show_history():
    """Print the full conversation history in a readable format."""
    print("\n" + "=" * 50)
    print("  📜  CONVERSATION HISTORY")
    print("=" * 50)
    for i, msg in enumerate(history):
        role = msg["role"].capitalize()
        content = msg["content"]
        if role != "System":
            print(f"[{i}] {role}: {content}")
    print("=" * 50 + "\n")
