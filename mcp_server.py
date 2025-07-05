import os
import sys
import logging
from dotenv import load_dotenv # Import load_dotenv
from mcp.server.fastmcp import FastMCP  # Import FastMCP
from pydantic import BaseModel, Field
from elevenlabs.client import ElevenLabs

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    logger.error("ELEVENLABS_API_KEY environment variable not set. Please set it in your .env file or environment.")
    sys.exit(1) # Exit if API key is not set

elevenlabs_client = ElevenLabs(api_key=api_key)

# Initialize FastMCP server (replace "elevenlabs" with a meaningful server name)
mcp_server = FastMCP("elevenlabs_tts_server")

# Define the input model for your tool
class SpeakToolInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, description="The text to convert to speech.")
    model_id: str = Field("eleven_flash_v2_5", description="The ID of the Eleven Labs model to use.")
    voice_id: str = Field("Z3R5wn05IrDiVCyEkUrK", description="The ID of the Eleven Labs voice to use.")

# Define the output for your tool. This is simplified;
# in a real MCP server, you'd return a path/URL to a resource or
# handle streaming as per MCP's resource/tool output spec.
# For simplicity, let's say it returns a base64 encoded string or a temporary URL.
# The MCP SDK would usually handle the streaming part.
class SpeakToolOutput(BaseModel):
    success: bool = Field(True, description="Indicates that the text was successfully spoken.")
    
@mcp_server.tool()
async def speak_text_to_audio(request: SpeakToolInput) -> SpeakToolOutput:
    """
    Converts text to speech using Eleven Labs and plays it.
    """
    logger.info(f"MCP Tool: Received speak request for voice_id: {request.voice_id}, model_id: {request.model_id}")
    try:
        audio_stream_iterator = elevenlabs_client.text_to_speech.convert(
            text=request.text,
            voice_id=request.voice_id,
            model_id=request.model_id,
            output_format="mp3_44100_128"
        )

        # Since this is a side-effect-only tool, we consume the stream to ensure the API call is made,
        # but we don't need to store or return the audio data.
        for _ in audio_stream_iterator:
            pass

        logger.info("Text-to-speech conversion successful.")
        return SpeakToolOutput(success=True)

    except Exception as e:
        logger.exception(f"An unexpected error occurred during text-to-speech: {e}")
        raise Exception(f"An internal server error occurred: {str(e)}")

# This part is where the FastMCP server runs, NOT Uvicorn directly
if __name__ == "__main__":
    stdio_command = [sys.executable, os.path.abspath(__file__)]
    try:
        mcp_server.run()
    except Exception as e:
        logger.exception(f"Failed to start MCP server: {e}")
        sys.exit(1) # Exit with an error code
