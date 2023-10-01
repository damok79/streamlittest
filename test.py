import streamlit as st

# Check if 'chat_log' is already in the session state
if 'chat_log' not in st.session_state:
    # If not, initialize it as an empty list
    st.session_state['chat_log'] = []

def chatbot():
    st.title("Simple Echo Chatbot")

    # Create placeholders for the chat log and the user input
    chat_placeholder = st.empty()
    input_placeholder = st.empty()

    # Get user input
    user_input = input_placeholder.text_input("Enter your message")

    if st.button("Send"):
        # Append user message and bot response to chat log
        st.session_state.chat_log.append(f"You: {user_input}")
        st.session_state.chat_log.append(f"Bot: {user_input}")

        # Display chat log
        for message in st.session_state.chat_log:
            chat_placeholder.write(message)

    # Add custom CSS to change the color of the text entry box
    st.markdown("""
    <style>
    .stTextInput input {
        background-color: #fafafa;
    }
    </style>
    """, unsafe_allow_html=True)

chatbot()
