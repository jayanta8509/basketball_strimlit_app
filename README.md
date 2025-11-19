# 🏀 Basketball League Chat Application

A modern, interactive chat application built with Streamlit that connects to the Basketball League API to provide information about team registrations, waitlists, bracket assignments, and contact information.

## Features

- 💬 **Interactive Chat Interface**: Clean, modern chat UI with conversation history
- 🎨 **Beautiful Design**: Gradient background with glassmorphism effects
- 🔄 **Real-time API Integration**: Connects to the Basketball League API
- 📱 **Responsive Layout**: Works seamlessly on desktop and mobile devices
- 🛡️ **Error Handling**: Robust error handling for network issues and API errors
- 🗑️ **Chat Management**: Clear chat history option

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd e:\basketball_strimlit_app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**:
   The application will automatically open in your default browser at `http://localhost:8501`

3. **Start chatting**:
   - Type your questions in the chat input at the bottom
   - Ask about team registrations, waitlists, brackets, or contact information
   - The assistant will respond with relevant information from the Basketball League API

## API Configuration

The application is configured to use the following API endpoint:
- **URL**: `https://nexusflowaimcp.bestworks.cloud/api/v1/basketball/ask-question`
- **Method**: POST
- **User ID**: `jayanta123` (hardcoded)

### API Request Format
```json
{
  "question": "your question here",
  "user_id": "jayanta123"
}
```

### API Response Format
```json
{
  "answer": "response from the API",
  "status": "success",
  "code": 200,
  "question": "your question here"
}
```

## Project Structure

```
e:\basketball_strimlit_app\
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **Streamlit**: Web framework for creating the chat interface
- **Requests**: HTTP library for making API calls
- **Python 3.7+**: Programming language

## Customization

You can customize the application by modifying:
- **User ID**: Change the `USER_ID` constant in `app.py`
- **API Endpoint**: Modify the `API_ENDPOINT` constant in `app.py`
- **Styling**: Update the CSS in the `st.markdown()` section
- **Welcome Message**: Edit the initial assistant message in the session state initialization

## Troubleshooting

- **Connection Error**: Ensure you have an active internet connection
- **API Timeout**: The request timeout is set to 30 seconds; check your network speed
- **Module Not Found**: Make sure all dependencies are installed via `pip install -r requirements.txt`

## License

This project is open source and available for educational and commercial use.

---

Made with ❤️ using Streamlit
