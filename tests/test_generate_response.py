from modules.generate_response import get_assistant_reply

def test_llama_response():
    reply = get_assistant_reply("Hello!")
    assert isinstance(reply, str)
    assert len(reply.strip()) > 0