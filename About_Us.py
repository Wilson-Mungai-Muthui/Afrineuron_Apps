import streamlit as st
from theme import footer

st.set_page_config(page_title="Afrineuron", page_icon="🧠", layout="wide")

col1, col2, col3 = st.columns(3)
with col2:
    st.image("https://afrineuron.files.wordpress.com/2023/06/afrineuron-1-10-2.png")
    st.markdown("<h2 style = 'text-align: center; color: white;'>Afrineuron🧠</h2>", unsafe_allow_html=True)

footer()

st.markdown("<h3 style = 'text-align: center; color: white;'>A Community Passionate about Transforming Africa</h3>", unsafe_allow_html=True)

st.markdown(
    """
The [Afrineuron](https://afrineuron.com/) founding team boasts a wealth of experience developing
and implementing AI solutions, with some being co-founders at legal-tech startup, [Waki.li](https://waki.li/), and one being a co-founder at climate-tech startup
Verst Carbon. Waki.li is Africa's first AI-powered legal consultant
providing legal advice to the underserved in Malawi, as well as a legal
research aide to lawyers.


It was their experience developing and deploying AI solutions that
brought about the idea of building a community to convene African
machine learning and artificial intelligence developers to collaborate on
practical AI solutions and applications that are geared towards impact.


[Afrineuron's](https://afrineuron.com/) community consists of talented AI practitioners who
collaborate to address complex real-world problems and create practical
AI/ML solutions & applications. These impact-driven projects are geared
towards fostering AI adoption in Africa and are devised using cutting edge technologies like Computer Vision and Natural Language
Processing (NLP) to tailor solutions to real African problems.


[Afrineuron](https://afrineuron.com/) has ambitious goals of developing a talent pool of over 10,000
AI practitioners across Africa, implementing over 100+ AI projects, and
spotlighting over 500 AI founders by 2025. This was informed by the
tremendous power AI holds to shape the future, Africa cannot afford to
be left behind.
"""
)

st.markdown("<h3 style = 'text-align: center; color: white;'>Solving complex real-world problems with practical AI/ML solutions</h3>", unsafe_allow_html=True)

st.markdown(
    """
[Afrineuron's](https://afrineuron.com/) AI projects span across several sectors, reflecting the
versatile and comprehensive nature of AI and how it can be applied to
various areas of life. One such project is an AI solution capable of
analyzing oceanographic data, such as water temperature, currents,
weather conditions, and historical catch data, to predict optimal fishing
times and zones. This initiative has the potential to revolutionize the
fisheries sector, helping fishermen maximize their yield while also
preserving marine ecosystems.
In agriculture, Afrineuron is creating an AI solution that leverages
OpenStreetMap data to aid farmers in effective and sustainable land
management. This project could transform the African agricultural sector,
offering farmers new tools to optimize their farming practices, increase
their yield, and ensure more sustainable farming methods.
In the field of environmental conservation, Afrineuron is working on
creating an AI model capable of analyzing satellite and geospatial data to
detect signs of deforestation, illegal mining, or other activities that could
harm natural ecosystems. This is an area where AI can play a vital role in
preserving Africa's rich biodiversity and natural resources . These are just
but a few of the projects in Afrineuron's portfolio.
"""
)

st.markdown("<h3 style = 'text-align: center; color: white;'>AI in Africa: The Road Ahead</h3>", unsafe_allow_html=True)

st.markdown(
    """
The rapid innovation and uptake of other technologies such as mobile
and financial technologies (fintech) like M-Pesa is a clear testament to
Africa's potential as a pioneer in technology. The success of mobile
technologies across Africa has permitted African nations to dramatically
increase their communication capabilities while leapfrogging the need
for old-fashioned infrastructure. AI holds the potential to provide several
multitudes more of an impact on not just livelihoods, but also
productivity.

""")

sidebar_content = """
    ## Afrineuron: Transforming Africa with AI Solutions
    Afrineuron is a dynamic community driven by experienced AI pioneers passionate about 
    harnessing artificial intelligence and machine learning to address Africa's challenges. 
    The team's expertise stems from ventures like Waki.li and Verst Carbon, inspiring the creation 
    of a collaborative platform to unite African AI developers. With goals to nurture over 10,000 
    AI practitioners, undertake 100+ impactful projects, and highlight 500 AI founders by 2025, 
    Afrineuron is dedicated to leveraging technologies like Computer Vision and NLP to devise 
    practical solutions for real-world issues. From predicting optimal fishing times to detecting 
    deforestation through AI, Afrineuron embodies Africa's potential as a technological trailblazer, 
    leading the way towards innovation and progress on the continent.
    """
st.sidebar.markdown(sidebar_content)