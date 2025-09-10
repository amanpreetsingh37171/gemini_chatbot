import streamlit as st
import google.generativeai as genai
import webbrowser

# --- Initialize session state ---
if "chat_data" not in st.session_state:
    st.session_state.chat_data = []

# --- Configure Gemini API safely ---
if "GEMINI" not in st.secrets or "api_key" not in st.secrets["GEMINI"]:
    st.error("❌ Gemini API key is missing. Please add it in Streamlit Cloud → Settings → Secrets.")
    st.stop()  # Stop execution if no key
else:
    genai.configure(api_key=st.secrets["GEMINI"]["api_key"])
    model = genai.GenerativeModel("gemini-2.5-flash")

# --- UI ---
st.header("🤖 My Personal AI Chatbot")
st.subheader("Ask me anything!")

user_input = st.chat_input("Write your query")

if user_input:
    st.session_state.chat_data.append(("User", user_input))

    if "who build you" in user_input.lower() or "who developed you" in user_input.lower():
        response = "I am an AI chatbot developed by Aman."
        st.session_state.chat_data.append(("AI", response))

    elif "open youtube" in user_input.lower():
        webbrowser.open("https://www.youtube.com")
        response = "📺 Opening YouTube for you!"
        st.session_state.chat_data.append(("AI", response))

    elif "open google" in user_input.lower():
        webbrowser.open("https://www.google.com")
        response = "🌐 Opening Google for you!"
        st.session_state.chat_data.append(("AI", response))

    else:
        response = model.generate_content(user_input)
        st.session_state.chat_data.append(("AI", response.text))

# --- Display Chat ---
for key, data in st.session_state.chat_data:
    with st.chat_message(key):
        st.markdown(data)
