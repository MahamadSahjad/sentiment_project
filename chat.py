import streamlit as st
from bot import simple_chat_bot

st.set_page_config(page_title="Simple NLP Chatbot", layout="centered")
st.title("Simple chatbot with NLP")
st.markdown("Type a message below and let's chat!")

if "message" not in st.session_state:
    st.session_state.message = []

user_input = st.text_input("You", key="input")

if user_input:
    st.session_state.message.append(("You", user_input))
    response = simple_chat_bot(user_input)
    st.session_state.message.append(("Bot", response))

for sender, msg in st.session_state.message:
    if sender == "You":
        st.markdown(f"**{sender}:** {msg}")
    else:
        st.markdown(f"**{sender}:** {msg}")
