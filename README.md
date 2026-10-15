# AI Voice Assistant

A lightweight, voice-enabled AI assistant built in Python that listens to user speech, sends the prompt to a local large language model, and speaks the response back using text-to-speech. The project is designed as a practical foundation for voice-driven workflows and can be extended into a more production-ready conversational application.

## Overview

This repository demonstrates a simple conversational pipeline:

- Speech input via microphone or keyboard fallback
- Local LLM inference through Ollama
- Text-to-speech output using `pyttsx3`
- Conversation logging for debugging and auditability
- Basic test coverage for response generation

The current implementation is an excellent starting point for a prototype or internal tool, and it can be hardened for production use with configuration management, model abstraction, observability, persistence, and deployment automation.

## Features

- Voice capture and transcription using `SpeechRecognition`
- Local AI response generation with Ollama (`llama2` by default)
- Real-time text-to-speech playback
- Mock fallback response when the local model is unavailable
- Conversation log stored in `assistant_log.txt`
- Keyboard input fallback if the microphone is unavailable
- Basic automated test for assistant reply generation

## Repository Structure

```text
AI-Voice-Assistant/
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── assistant_log.txt           # Conversation history log
├── LLM1.ipynb                 # Notebook experiments and exploration
├── modules/
│   ├── generate_response.py   # LLM request and fallback logic
│   ├── speech_input.py        # Audio capture and transcription
│   ├── text_to_speech.py      # Speech synthesis
│   └── utils.py               # Logging utilities
├── tests/
│   └── test_generate_response.py
├── .vscode/                   # Editor configuration
└── README.md                  # Project documentation
```

## Tech Stack

- Python 3.10+
- `speechrecognition` for microphone input
- `pyttsx3` for text-to-speech
- `requests` for communicating with Ollama
- `pytest` for testing
- Ollama local inference server

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 or newer installed
- A working microphone (recommended for voice interaction)
- Ollama installed and running locally
- Access to a local LLM model such as `llama2`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sai-Niresh/Ai-Voice-Assistant.git
cd Ai-Voice-Assistant
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install and start Ollama:

```bash
ollama pull llama2
ollama serve
```

If Ollama is not already installed, download it from the official Ollama website and configure it locally.

5. On Linux systems, you may need TTS dependencies for `pyttsx3` to work correctly:

```bash
sudo apt-get update
sudo apt-get install espeak-ng
```

## Running the Assistant

Launch the application:

```bash
python main.py
```

Once running, the assistant will listen for speech input. You can either:

- Speak into the microphone, or
- Type a prompt when the microphone is unavailable

To exit the app, say or type:

```text
stop
```

## How It Works

The application follows a straightforward pipeline:

1. `main.py` starts the voice assistant loop.
2. `modules/speech_input.py` listens to the microphone and converts speech to text.
3. `modules/generate_response.py` sends the user prompt to the local Ollama endpoint.
4. The model response is returned and printed to the console.
5. `modules/text_to_speech.py` reads the response aloud.
6. `modules/utils.py` logs the interaction into `assistant_log.txt`.

## Configuration

The project currently uses a direct local endpoint:

```python
http://localhost:11434/api/generate
```

and the default model is:

```python
llama2
```

If you want to make the project more production ready, consider moving these values into:

- environment variables
- a `config.yaml` file
- a dedicated settings module
- model provider abstraction

## Testing

Run the project tests with:

```bash
pytest
```

The current test validates that the assistant reply returns a non-empty string.

## Logging and Monitoring

Conversation logs are written to `assistant_log.txt` with timestamps and mode information. This is useful for:

- debugging model behavior
- reviewing user interactions
- monitoring fallback usage
- identifying failure points

For production use, this should evolve into:

- structured JSON logging
- centralized log aggregation
- metrics collection
- error tracking and alerting

## Production Readiness Considerations

This prototype is functional, but to bring it closer to a production-grade application, consider the following improvements:

### 1. Configuration Management
- Move model names, API URLs, and audio settings into environment-based configuration.
- Support multiple models and providers.

### 2. Robust Error Handling
- Add retries for Ollama connectivity failures.
- Gracefully handle microphone errors, permission issues, and unsupported audio devices.
- Provide actionable user feedback instead of silent failures.

### 3. Session and Conversation Memory
- Add persistent memory between conversation turns.
- Support contextual follow-ups and long-running sessions.
- Control token usage and conversation history growth.

### 4. Security and Privacy
- Avoid storing sensitive voice data unnecessarily.
- Sanitize logs and redact user information in production.
- Define retention policies for transcript storage.

### 5. Performance and Scalability
- Move blocking operations to background workers when needed.
- Consider asynchronous response pipelines.
- Add queue-based processing for high-volume workloads.

### 6. Deployment
- Package the application as a service or CLI tool.
- Add Docker support for easier deployment.
- Create a health check and dependency verification step.

## Example Workflow

```text
User: "Hello, can you help me summarize this project?"
Assistant: "Certainly — here is a brief summary of the repository..."
```

The system captures the speech, generates a response, and speaks the answer aloud.

## Troubleshooting

### Ollama connection errors

If the assistant falls back to the mock response, confirm that:

```bash
ollama serve
```

is running and that the `llama2` model is available locally.

### Microphone not working

Check that:

- the microphone is connected and enabled
- operating system permissions are granted
- the correct input device is selected

### TTS not speaking

Ensure the system has audio support and that the `pyttsx3` engine can initialize correctly. On some systems, installing `espeak` or the required OS speech package is necessary.

## Future Enhancements

- Add support for multiple LLM providers
- Add wake-word activation
- Improve command handling for voice actions
- Integrate web or database backends
- Add authentication and user profiles
- Build a web dashboard for monitoring and analytics

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes with clear documentation
4. Add or update tests
5. Open a pull request with a concise explanation

## Notes

This project is designed as a practical AI voice assistant prototype using local inference and open-source tooling. It is a strong foundation for experimentation, learning, and product exploration, and it can be expanded into a production-ready voice assistant with stronger architecture, monitoring, and deployment practices.

