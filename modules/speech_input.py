import speech_recognition as sr

def get_speech_input():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening...")
            audio = r.listen(source)
        said = r.recognize_google(audio)
        print(f"You said: {said}")
        return said
    except Exception:
        # Fallback to keyboard input
        return input("⌨️ Mic not available. Type your question: ")