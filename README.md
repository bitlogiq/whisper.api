# Whisper API

FastAPI service to run OpenAI Whisper transcription via REST.

## Usage

```
curl -X POST -F "file=@your_audio.ogg" https://<your-deployed-url>/transcribe
```

Returns JSON: `{"text": "your transcription"}`
