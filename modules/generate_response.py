import requests
import json

# Store conversation history
conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def get_assistant_reply(prompt: str) -> str:
    # Add user message to history
    conversation.append({"role": "user", "content": prompt})

    # Format history into a single prompt for Ollama
    full_prompt = ""
    for msg in conversation:
        if msg["role"] == "user":
            full_prompt += f"User: {msg['content']}\n"
        elif msg["role"] == "assistant":
            full_prompt += f"Assistant: {msg['content']}\n"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama2", "prompt": full_prompt},
            stream=True
        )

        reply = ""
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode("utf-8"))
                    reply += chunk.get("response", "")
                except json.JSONDecodeError:
                    continue

        conversation.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        print("❌ Local LLM Error:", e)
        reply = f"(Mock Assistant Fallback) You said: {prompt}"
        conversation.append({"role": "assistant", "content": reply})
        return reply