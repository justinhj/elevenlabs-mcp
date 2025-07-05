# ElevenLabs Text-to-Speech MCP Server

This project provides a simple server that exposes ElevenLabs' text-to-speech functionality as a tool using the FastMCP framework.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/elevenlabs-mcp-server.git
    cd elevenlabs-mcp-server
    ```

2.  **Install dependencies:**
    Make sure you have Python 3.12 or higher installed. You can use `uv` to install the dependencies:
    ```bash
    uv pip install -r requirements.txt
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

## Usage

1.  **Run the server:**
    You can run the server in two ways:

    *   **STDIO:**
        ```bash
        python elevenlabs_mcp.py
        ```

    *   **HTTP:**
        ```bash
        uvicorn mcp_server:server --host 127.0.0.1 --port 9000
        ```

2.  **Send a request to the server:**
    You can use the provided `example1.py` to send a request to the server. Make sure the server is running in HTTP mode.

    ```bash
    python example1.py
    ```

    This will send a request to the server to say "Hello, world!" using the default voice. You can customize the text and `voice_id` in the `example1.py` file.
