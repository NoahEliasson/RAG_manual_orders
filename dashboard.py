import streamlit as st
from backend.backend_rag import get_response

# Page title with styling
st.set_page_config(page_title="RAG Manual Orders Chatbot", layout="centered")
st.title("RAG Manual Orders")

# Add a description or instructions
st.markdown(
"""test rag""")

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")

# Input box for user prompt
with st.form(key="chat_form"):
    user_input = st.text_input("Type your question:", placeholder="Ask me anything about manual orders...")
    submit_button = st.form_submit_button("Send")

# Handle user input
if submit_button and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Fetch response from backend
    with st.spinner("loading..."):
        bot_response = get_response(user_input)

    # Add bot response to chat history
    st.session_state.messages.append({"role": "bot", "content": bot_response})
