import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elevenlabs import generate, set_api_key
from elevenlabs.client import ElevenLabs
from fastapi.responses import StreamingResponse
import uvicorn

# Check for the API key
api_key = os.getenv("ELEVEN_API_KEY")
if not api_key:
    raise ValueError("ELEVEN_API_KEY environment variable not set")

set_api_key(api_key)
client = ElevenLabs()

app = FastAPI()

class SpeakRequest(BaseModel):
    text: str
    model_id: str = "eleven_multilingual_v2"
    voice_id: str = "21m00Tcm4TlvDq8ikWAM"

@app.post("/speak")
async def speak(request: SpeakRequest):
    """
    Receives text and optional model/voice IDs, and streams back the generated audio.
    """
    try:
        audio_stream = client.generate(
            text=request.text,
            voice=request.voice_id,
            model=request.model_id,
            stream=True
        )
        return StreamingResponse(audio_stream, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
