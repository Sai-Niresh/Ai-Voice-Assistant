
from modules.speech_input import get_speech_input
from modules.generate_response import get_assistant_reply
from modules.text_to_speech import speak_text
from modules.utils import log_to_file

# Load environment variables


def main():
    print("🎙️ AI Voice Assistant is running... (type 'stop' to quit)")

    while True:
        user_input = get_speech_input()
        if not user_input:
            continue  # if nothing was said/typed, keep listening

        if "stop" in user_input.lower():
            print("👋 Exiting assistant. Goodbye!")
            break

        reply = get_assistant_reply(user_input)
        mode = "mock" if reply.startswith("(Mock") else "real"
        log_to_file(user_input, reply, mode)
        print("🤖 Assistant:", reply)
        speak_text(reply)

if __name__ == "__main__":
    main()