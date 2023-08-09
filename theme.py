import streamlit as st

def footer():
    hide_streamlit_style = """
                <style>
                
                footer {visibility: hidden;}              
                footer:after {
                    content:'Powered by Afrineuron'; 
                    visibility: visible;
                    display: block;
                    position: centre;
                    #background-color: red;
                    padding: 5px;
                    top: 2px;
                    .sidebar .sidebar-content {
                    background-image: linear-gradient(#2e7bcf,#2e7bcf);
                    color: white;}
            }
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)