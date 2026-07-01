from openai import OpenAI
from config import GEMINI_API_KEY, GEMINI_BASE_URL, MODEL_NAME
from memory import get_history, add_user_message, add_assistant_message

# Initialise the OpenAI client once, pointing to Gemini's compatibility endpoint
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL
)


def send_message(user_input: str) -> str:
    """
    1. Add the user's message to history
    2. Send the full history to the OpenAI API
    3. Receive the AI reply
    4. Store the reply in history
    5. Return the reply text
    """

    # Step 1 – remember what the user said
    add_user_message(user_input)

    # Step 2 & 3 – call the API with the full conversation history
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=get_history()
    )

    # Step 4 – extract the text reply
    reply = response.choices[0].message.content

    # Step 5 – remember the assistant's reply
    add_assistant_message(reply)

    return reply
