import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ── API Settings ──────────────────────────────────────────────
GEMINI_API_KEY = os.getenv("Gemini_API_KEY") or os.getenv("gemini_API_KEY")
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

# ── Model Settings ────────────────────────────────────────────
MODEL_NAME = "gemini-2.5-flash"   # Using Gemini 2.5 Flash via compatibility layer

# ── Chatbot Personality ───────────────────────────────────────
SYSTEM_PROMPT = (
    "You are a helpful, friendly, and intelligent AI assistant. "
    "You remember everything discussed in this conversation and give "
    "clear, concise, and accurate answers."
)

# ── Display Settings ──────────────────────────────────────────
BOT_NAME  = "AI Assistant"
USER_NAME = "You"
