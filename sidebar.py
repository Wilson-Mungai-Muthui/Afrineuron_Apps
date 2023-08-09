import streamlit as st

from faq import faq
from dotenv import load_dotenv
import os

load_dotenv()

def sidebar():
    with st.sidebar:
        st.markdown(
            "# How To Use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖AskYourPDF allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress💡\n"
            "## 🔧 Features\n"
            
            "- Upload documents 📁(PDF, DOCX, TXT) and answer questions about them.\n"
            "- Cite sources📚 for the answers, with excerpts from the text.\n"

            "## 🚀 Upcoming Features\n"

            "- Add support for more formats (e.g. webpages 🕸️, PPTX 📊, etc.)\n"
            "- Highlight relevant phrases in citations 🔦\n"
            "- Support scanned documents with OCR \n📝"
            "- More customization options (e.g. chain type 🔗, chunk size📏, etc.)\n"
            "- Chat with multiple pdfs\n"
        )
        st.markdown("---")

        faq()
