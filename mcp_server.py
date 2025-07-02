import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elevenlabs.client import ElevenLabs
from fastapi.responses import StreamingResponse
import uvicorn

# Check for the API key
api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(api_key=api_key)

app = FastAPI()

class SpeakRequest(BaseModel):
    text: str
    model_id: str = "eleven_flash_v2_5"
    voice_id: str = "Z3R5wn05IrDiVCyEkUrK"

@app.post("/speak")
async def speak(request: SpeakRequest):
    """
    Receives text and optional model/voice IDs, and streams back the generated audio.
    """
    try:
        audio_stream = client.text_to_speech.convert(
            text=request.text,
            voice_id=request.voice_id,
            model_id=request.model_id,
            output_format="mp3_44100_128"
        )
        return StreamingResponse(audio_stream, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
