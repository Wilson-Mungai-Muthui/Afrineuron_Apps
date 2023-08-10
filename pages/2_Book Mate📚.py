import streamlit as st
import PyPDF2
import base64
from langchain.document_loaders import PyPDFLoader
import recommendationsBot,queryBot,summarizer, translate
import api
import os
import openai
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from _api import get_audio
from theme import footer
from sidebar_PDFVoiceMate import sidebar
from ui import is_open_ai_key_valid

st.set_page_config(page_title="Book Mate", page_icon="📚", layout="wide")

sidebar()
col1, col2, col3 = st.columns(3)
with col2:
    st.image("https://afrineuron.files.wordpress.com/2023/06/afrineuron-1-10-2.png")
st.markdown("<h2 style = 'text-align: center; color: white;'>Book Mate📚</h2>", unsafe_allow_html=True)
footer()

openai_api_key = st.session_state.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key
openai.api_key = openai_api_key

if not openai_api_key:
    st.warning(
        "Enter your OpenAI API key in the sidebar. You can get a key at"
        " https://platform.openai.com/account/api-keys."
    )

if not is_open_ai_key_valid(openai_api_key):
    st.stop()

def pdf_content(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def file_upload():
    upload_file = st.file_uploader(
    "Upload a pdf, docx, or txt file",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!")
    return upload_file

def main():

    pdf_file = file_upload()

    if pdf_file is not None:
        pdf_contents = pdf_file.read()
        pdf_b64 = base64.b64encode(pdf_contents).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_b64}" width="500" height="800"></iframe>'
        st.sidebar.markdown(pdf_display, unsafe_allow_html=True)
        st.warning("PDF with more than 4mb can take time to load")
        data = pdf_content(pdf_file)
        os.makedirs("./Data",exist_ok=True)
        try:
            with open("./Data/output.text","w") as file:
                file.write(data)
        except UnicodeEncodeError as e:
            print(f"Error encoding character at position {e.start}: {e.object[e.start]}")
        file.close()
        
        st.header("Our features")
        feature = st.selectbox("Choose feature",("AudioBook powered by ElevenLabs🔊","Book Summarizer📝","QueryBot🤖","Book Recommendations📚"))
        
        if feature == "Book Summarizer📝":
            with st.spinner("Summarizing the PDF content. Please wait..."):
                st.write(summarizer.summarizeIt(data[100:4000],openai_api_key))

        if feature == 'AudioBook powered by ElevenLabs🔊':
            st.markdown("""AudioBook supports 5 different languages including: 
- English 
- Hindi
- French
- Spanish
- German
""")
            pick_lang = st.selectbox("Choose your preferred language",("English","Hindi","German","Spanish","French"))
            listen_button = st.selectbox("How can I help?",["Generate PDF Summary Audio","Read out particular topic"])
            available_voices = st.selectbox("Select a voice",("Bella","Sam","Antoni","Elli","Adam",'Rachel','Domi'))
            
            if listen_button == 'Generate PDF Summary Audio':
                with st.spinner("Summarizing the PDF content. Please wait..."):
                    text = summarizer.summarizeIt(data[100:800],openai_api_key)
                    if len(text) > 800:
                        st.warning("The limit is 800 words. We are processing audio for first 800 words")
                    text = text[0:800]
                if pick_lang == 'English':
                    with st.spinner("Converting into Audio..."):
                        st.audio(get_audio(text,available_voices))
                else:
                    with st.spinner("Translating your context"):
                        language_translation = translate.convert("en",pick_lang,text)
                        with st.spinner("Converting into Audio..."):
                            st.audio(get_audio(language_translation,available_voices))
                            
            elif listen_button == "Read out particular topic":
                topic = st.text_input("What topic you what to listen?")
                if topic:
                    with st.spinner("Finding best solution..."):
                        knowledge_base = queryBot.process_text(data,openai_api_key)
                        #memory = ConversationBufferMemory(memory_key="chat_history", input_key="input")
                        docs = knowledge_base.similarity_search(topic)
                        llm = OpenAI()
                        chain = load_qa_chain(llm, chain_type='stuff')
                        with get_openai_callback() as cost:
                            response = chain.run(input_documents=docs, question=topic)
                    with st.spinner("Converting into Audio..."):
                        if pick_lang == 'English':
                            st.audio(get_audio(response,available_voices))
                        else:
                            language_translation = translate.convert("en",pick_lang,response)
                            st.audio(get_audio(language_translation,available_voices))
                    
            
        if feature == 'QueryBot🤖':
            from streamlit_chat import message
            from streamlit_extras.colored_header import colored_header
            from streamlit_extras.add_vertical_space import add_vertical_space
            
            if 'generated' not in st.session_state:
                st.session_state['generated'] = ["I'm your Book Query Bot"]
            if 'past' not in st.session_state:
                st.session_state['past'] = ['How can you help me?']
                
            input_container = st.container()
            colored_header(label='', description='', color_name='red-30')
            response_container = st.container()
            
            def get_text():
                input_text = st.text_input("You: ", "", key="input")
                return input_text
            
            with input_container:
                query = get_text()
            
            def generate_response(prompt):
                knowledge_base = queryBot.process_text(data,openai_api_key)
                #memory = ConversationBufferMemory(memory_key="chat_history", input_key="input")
                docs = knowledge_base.similarity_search(query)
                llm = OpenAI()
                chain = load_qa_chain(llm, chain_type='stuff')
                with get_openai_callback() as cost:
                    response = chain.run(input_documents=docs, question=query)
                return response
            
            with response_container:
                if query:
                    response = generate_response(query)
                    st.session_state.past.append(query)
                    st.session_state.generated.append(response)
                    
                if st.session_state['generated']:
                    for i in range(len(st.session_state['generated'])):
                        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
                        message(st.session_state["generated"][i], key=str(i))
                
        if feature == 'Book Recommendations📚':
            with st.form(key='my_form'):
                user_prompt = st.text_input("What kind of book recommendation you need?")
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    with st.spinner("Fetching recommendations. Please wait..."):
                        st.write(recommendationsBot.get_recommendations(user_prompt,openai_api_key))
                
if __name__ == "__main__":
    main()