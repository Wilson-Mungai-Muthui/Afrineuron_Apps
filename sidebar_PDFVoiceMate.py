import streamlit as st
import os

def sidebar():
    with st.sidebar:
        st.markdown(
            "# How To Use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"
        )

        api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="Paste your OpenAI API key here (sk-...)",
        help="You can get your API key from https://platform.openai.com/account/api-keys.",
        value=os.environ.get("OPENAI_API_KEY", None)
        or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input        
        
        st.markdown(
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Decide and choose which feature you want to use based on your needs:\n"
            "- **Summarize📝:** If you want a shorter version of the PDF content.\n"
            "- **AudioBook🔊:** If you'd like the content to be read aloud like an audiobook.\n"
            "- **QueryBot🤖:** If you have questions and want the app to help you find answers.\n"
            "- **Book Recommendations📚:** If you're interested in discovering new books.\n"
            "4. Follow the instructions of each feature:\n"
            "- **Summarize:** The app provides a summarized version\n"
            "- **AudioBook:** Select language, audio type,decide whether you want to generate an audio summary or read out a specific topic, and voice. Listen to the audio\n"
            "- **QueryBot:** Ask a question, and the app gives you an answer.\n"
            "- **Book Recommendations:** Input preferences, get book suggestions.\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
        """ 
        PDF Voice Mate is an innovative and versatile application designed to 
        revolutionize the way you interact with PDF files. With a range of powerful features, 
        this app aims to simplify and enhance your experience when working with PDF documents of all kinds. 
        Whether you're a student, professional, or simply someone who deals with PDFs regularly, 
        PDF Voice Mate is here to make your tasks more efficient, convenient, and engaging.
        """
        )
        st.markdown("---")
        