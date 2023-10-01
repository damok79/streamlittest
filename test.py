import streamlit as st

# Check if 'chat_log' is already in the session state
if 'chat_log' not in st.session_state:
    # If not, initialize it as an empty list
    st.session_state['chat_log'] = []

# Check if 'user_input' is already in the session state
if 'user_input' not in st.session_state:
    # If not, initialize it as an empty string
    st.session_state['user_input'] = ""

def chatbot():
    st.title("Capybot v0.01")

    # Create placeholders for the chat log and the user input
    chat_placeholder = st.empty()
    input_placeholder = st.empty()

    # Get user input
    st.session_state['user_input'] = input_placeholder.text_input("Enter your message", value=st.session_state['user_input'])

    if st.button("Send"):
        # Append user message and bot response to chat log
        st.session_state.chat_log.append(f"You: {st.session_state['user_input']}")
        st.session_state.chat_log.append(f"Bot: {st.session_state['user_input']}")

        # Clear user input
        st.session_state['user_input'] = ""

        # Display chat log
        chat_placeholder.markdown("\n".join(st.session_state.chat_log))

    # Add custom CSS to change the color of the text entry box
    st.markdown("""
    <style>
    .stTextInput input {
        background-color: #d3d3d3;
    }
    </style>
    """, unsafe_allow_html=True)

chatbot()
