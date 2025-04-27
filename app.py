import streamlit as st
import requests
import json

st.set_page_config(
    page_title="LM Studio Client",
    page_icon="🤖",
    layout="wide"
)

# Sidebar for configuration
with st.sidebar:
    st.title("🤖 LM Studio Client")
    api_base = st.text_input(
        "API Base URL",
        value="http://localhost:1234/v1",
        help="LM Studio API base URL"
    )
    
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful AI assistant.",
        help="Set the system prompt for the model"
    )
    
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        help="Controls randomness in the response"
    )
    
    max_tokens = st.number_input(
        "Max Tokens",
        min_value=1,
        max_value=4096,
        value=2000,
        help="Maximum number of tokens in the response"
    )

# Main chat interface
st.title("Chat with LM Studio Model")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to ask?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepare the API request
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "messages": [
            {"role": "system", "content": system_prompt}
        ] + st.session_state.messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False
    }
    
    # Show spinner while waiting for response
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                f"{api_base}/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                assistant_response = response.json()["choices"][0]["message"]["content"]
                
                # Add assistant response to chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": assistant_response}
                )
                
                # Display assistant response
                with st.chat_message("assistant"):
                    st.markdown(assistant_response)
            else:
                st.error(f"Error: API returned status code {response.status_code}")
                st.error(response.text)
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to LM Studio API: {str(e)}")
            st.info("Make sure LM Studio is running and the API is enabled in the settings.")

# Add a clear button to reset the chat
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun() 