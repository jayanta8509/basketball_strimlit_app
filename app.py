import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Basketball League Chat",
    page_icon="🏀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# API Configuration
API_ENDPOINT = "https://nexusflowaimcp.bestworks.cloud/api/v1/basketball/ask-question"
USER_ID = "jayanta123"

# Custom CSS for better styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main-title {
        text-align: center;
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    div[data-testid="stChatMessageContent"] {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 10px;
    }
    div[data-testid="stChatInput"] {
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-title">🏀 Basketball League Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask me anything about team registrations, waitlists, brackets, and contact information!</p>', unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! 👋 Welcome to the Basketball League Assistant. I can help you with team registrations, waitlists, bracket assignments, and contact information. How can I assist you today?"
    })

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🏀" if message["role"] == "assistant" else "👤"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Display assistant response with loading indicator
    with st.chat_message("assistant", avatar="🏀"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking... 🤔")
        
        try:
            # Make API request
            payload = {
                "question": prompt,
                "user_id": USER_ID
            }
            
            response = requests.post(
                API_ENDPOINT,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            # Check if request was successful
            if response.status_code == 200:
                data = response.json()
                
                if data.get("status") == "success" and "answer" in data:
                    assistant_response = data["answer"]
                else:
                    assistant_response = "I received a response, but couldn't extract the answer. Please try again."
            else:
                assistant_response = f"Sorry, I encountered an error (Status code: {response.status_code}). Please try again."
        
        except requests.exceptions.Timeout:
            assistant_response = "The request timed out. Please try again."
        except requests.exceptions.ConnectionError:
            assistant_response = "Could not connect to the server. Please check your internet connection."
        except Exception as e:
            assistant_response = f"An unexpected error occurred: {str(e)}"
        
        # Display the response
        message_placeholder.markdown(assistant_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Add a clear chat button in the sidebar
with st.sidebar:
    st.markdown("### 🏀 Chat Options")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! 👋 Welcome to the Basketball League Assistant. I can help you with team registrations, waitlists, bracket assignments, and contact information. How can I assist you today?"
        }]
        st.rerun()
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("This chat application connects to the Basketball League API to provide information about:")
    st.markdown("- Team Registrations")
    st.markdown("- Waitlists")
    st.markdown("- Bracket Assignments")
    st.markdown("- Contact Information")
