from datetime import datetime

def log_to_file(user_input: str, reply: str, mode: str = "real", filename: str = "assistant_log.txt"):
    """
    Logs the conversation turn with timestamp and mode (real or mock).
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] Mode: {mode}\n")
            f.write(f"User: {user_input}\n")
            f.write(f"Assistant: {reply}\n\n")
    except Exception as e:
        print(f"⚠️ Logging Error: {e}")