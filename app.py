#Core Pkgs
import streamlit as st

#NLP Pkgs
import spacy_streamlit
from spacy import displacy
# import en_core_web_sm
import spacy
nlp = spacy.load('F:\MODEL_WEIGHTS\model-best\content\model-best')

#Web Scraping Pkgs
from bs4 import BeautifulSoup
from urllib.request import urlopen

import docx2txt


def main():
    """A Simple NLP App with Spacy-Streamlit"""
    st.title("Named Entity Recognition for Contract Dataset")

    menu = ["NER","NER for word documents"]
    choice = st.sidebar.radio("Pick a choice", menu)


    if choice == "NER":
        raw_text = st.text_area("Enter Text","")
        if raw_text != "":
            docx = nlp(raw_text)
            spacy_streamlit.visualize_ner(docx, labels = nlp.get_pipe('ner').labels)
    elif choice == "NER for word documents":
        docx_file = st.file_uploader("Upload a contract document in docx format: ",type=["docx"])
        if docx_file != "":
            # docx_file.type == 'text\plain'
            # st.subheader("Soon you will get chance to extract entites from word documents too!")
            raw_text = docx2txt.process(docx_file)
            docx_file = nlp(raw_text)
            spacy_streamlit.visualize_ner(docx_file, labels = nlp.get_pipe('ner').labels)
            
            # st.write(raw_text)
            # st.text(raw_text)
        

                



if __name__ == '__main__':
    main()
