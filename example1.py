import os
import sys
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python example1.py <text_to_speak>")
        sys.exit(1)

    text_to_speak = sys.argv[1]

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
            print(f"Successfully generated and played audio for: '{text_to_speak}'")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
