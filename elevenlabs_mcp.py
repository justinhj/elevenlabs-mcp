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
    name="greet",
    description="Greet a user by name using ElevenLabs text-to-speech. It returns a status message based on the api response"
)

def greet(name: str) -> str:
    """Greet a user by name."""
    text_to_speak = f"Hello, {name}, you big fanny!"
    try:
        audio = elevenlabs.text_to_speech.convert(
            text=text_to_speak,
            voice_id="Z3R5wn05IrDiVCyEkUrK",  # "JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_flash_v2_5",
            # "eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        if audio:
            play(audio)
            return '{"status": "OK"}'
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    mcp.run()
    
    # To use a different transport, e.g., Streamable HTTP:
    # mcp.run(transport="http", host="127.0.0.1", port=9000)
