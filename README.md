# LM Studio Web Client

A Streamlit-based web interface for interacting with LM Studio's local API. This application allows you to chat with your locally running LM Studio models through a user-friendly web interface.

## Prerequisites

- Python 3.8 or higher
- LM Studio installed and running on your computer
- LM Studio API enabled (make sure to enable it in LM Studio settings)

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure LM Studio is running and the API is enabled:
   - Open LM Studio
   - Go to Settings
   - Enable Local API Server
   - Note the API URL (default is http://localhost:1234)

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Features

- Clean and intuitive chat interface
- Configurable system prompt
- Adjustable temperature and max tokens
- Chat history with markdown support
- Error handling and status messages
- Clear chat functionality

## Configuration

You can configure the following parameters in the sidebar:
- API Base URL: The URL where LM Studio API is running
- System Prompt: The initial prompt that sets the AI's behavior
- Temperature: Controls response randomness (0.0 to 2.0)
- Max Tokens: Maximum length of the model's response

## Troubleshooting

If you encounter connection errors:
1. Verify that LM Studio is running
2. Check if the API is enabled in LM Studio settings
3. Confirm the API Base URL matches your LM Studio settings
4. Ensure no firewall is blocking the connection #   C h a t - w i t h - L M - S t u d i o - M o d e l  
 