from fastmcp import FastMCP
import os
import sys
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

mcp = FastMCP(name="MyServer")

@mcp.tool(
    name="speak",
    description="Play synchronously the text provided using ElevenLabs text-to-speech given an optional voice_id. It returns a status message based on the api response. If the status is ok then it worked, but if it the status is error there will be a message in the response too."
)
def speak(text: str, voice_id: str ="Z3R5wn05IrDiVCyEkUrK") -> dict[str, str]:
    try:
        audio = elevenlabs.text_to_speech.convert(
            text=text,
            voice_id=voice_id,  # "JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_flash_v2_5",  # "eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        if audio:
            play(audio)
            return {"status": "OK"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    mcp.run()
    
    # To use a different transport, e.g., Streamable HTTP:
    # mcp.run(transport="http", host="127.0.0.1", port=9000)
