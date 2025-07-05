# ElevenLabs Text-to-Speech MCP Server

This project provides a simple server that exposes ElevenLabs' text-to-speech functionality as a tool using the FastMCP framework.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/justinhj/elevenlabs-mcp.git
    cd elevenlabs-mcp
    ```

2.  **Install dependencies:**
    Make sure you have Python 3.12 or higher installed. You can use `uv` to install the dependencies:
    ```bash
    uv sync
    ```

## Configuration

1.  **Create a `.env` file:**
    ```bash
    touch .env
    ```

2.  **Add your ElevenLabs API key to the `.env` file:**
    ```
    ELEVENLABS_API_KEY="your-api-key"
    ```

Optionally you can set up an environment variable to store your ElevenLabs API key.

## Usage

Configure the mcp server as appropriate for your mcp client. For example if using Gemini-cli you can add the following to your `../gemini/settings.json`

```
{
    "mcpServers": {
        "elevenlabs_mcp": {
            "command": "uv",
            "args": [
                "run",
                "elevenlabs_mcp.py"
            ],
            "cwd": "/Users/yourhome/elevenlabsapi"
        }
    }
}
```

## Future Ideas

*   Allow customization of the voice and model via environment variables.
