import streamlit as st
from langchain.memory import ConversationBufferMemory
# Assume the necessary 'get_chat_response' function is in 'utils.py'
from utils import get_chat_response

st.title("Clone Chatgpt")
with st.sidebar:
    open_ai_key = st.text_input("OpenAI API Key", type="password")
    st.markdown("Get your OpenAI API key at https://platform.openai.com/")
    if st.button("Reset Conversation"):
        # Clear memory and messages
        st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
        st.session_state["messages"] = []

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "ai", "content": "Hello, I am chatgpt, I can answer your questions"}]

# Display messages
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not open_ai_key:
        st.info("Please enter OpenAI API key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("Thinking..."):
        response = get_chat_response(prompt, st.session_state["memory"], open_ai_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
