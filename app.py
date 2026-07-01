from chatbot import send_message
from memory import clear_history, show_history
from config import BOT_NAME, USER_NAME

# ── Banner ────────────────────────────────────────────────────
BANNER = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          🤖  AI CHATBOT  —  Powered by OpenAI           ║
║                                                          ║
║  Commands:                                               ║
║    quit / exit  →  End the conversation                  ║
║    clear        →  Reset conversation memory             ║
║    history      →  Show full conversation history        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""


def main():
    """Main loop — runs until the user types quit or exit."""

    print(BANNER)
    print(f"  {BOT_NAME} is ready! Start chatting below.\n")
    print("─" * 60)

    while True:
        try:
            # ── Get user input ────────────────────────────────
            user_input = input(f"\n{USER_NAME}: ").strip()

            # Skip empty input
            if not user_input:
                continue

            # ── Special commands ──────────────────────────────
            if user_input.lower() in ("quit", "exit"):
                print("\n👋  Goodbye! Have a great day!\n")
                break

            elif user_input.lower() == "clear":
                clear_history()
                continue

            elif user_input.lower() == "history":
                show_history()
                continue

            # ── Send to API and print response ────────────────
            print(f"\n{BOT_NAME}: ", end="", flush=True)
            reply = send_message(user_input)
            print(reply)
            print("\n" + "─" * 60)

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n👋  Interrupted. Goodbye!\n")
            break

        except Exception as e:
            print(f"\n❌  Error: {e}")
            print("    Please try again.\n")


# ── Entry Point ───────────────────────────────────────────────
if __name__ == "__main__":
    main()
