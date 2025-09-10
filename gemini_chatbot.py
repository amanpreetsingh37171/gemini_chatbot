import streamlit as st
import google.generativeai as genai
import webbrowser

if "chat_data" not in st.session_state:
    st.session_state.chat_data = []

st.write("Secrets available in Cloud:", dict(st.secrets))
genai.configure(api_key=st.secrets["GEMINI"]["api_key"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.header("My Personal AI Chatbot")

st.subheader("Ask me anything!")

user_input = st.chat_input("write your query")

if user_input:

    st.session_state.chat_data.append(("User", user_input))

    if "who build you" in user_input or "who developed you" in user_input:

        response = "I am AI Model developed by Aman"

        st.session_state.chat_data.append(("AI", response))


    elif "open Youtube" in user_input:
        webbrowser.open("https://www.youtube.com")

        response = "Opening YouTube for you!"

        st.session_state.chat_data.append(("AI", response))


    elif "open Google" in user_input:
        webbrowser.open("https://www.google.com")

        response = "Opening Google for you!"

        st.session_state.chat_data.append(("AI", response))

    else:
        response = model.generate_content(user_input)

        st.session_state.chat_data.append(("AI", response.text))


for key, data in st.session_state.chat_data:
    with st.chat_message(key):
        st.markdown(data)





