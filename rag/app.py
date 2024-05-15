import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyPDFLoader
import os
from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from retrievers import confluence_retriever
from retrievers import document_retriever
from generators import qa_generator
#from generators import summary_generators
from language_models import llmintf
def get_pdf_qa_response_generator():
    llm=llmintf.LLMIntf(llm_name="llama3")
    embedding=HuggingFaceEmbeddings()
    text_splitter=SemanticChunker(HuggingFaceEmbeddings())
    retriever=document_retriever.PDFRetriever(embedding,text_splitter)
    retriever.process_data_with_directory("/Users/ankurneog/projects/rag/data/personal")
    chat_response_generator=qa_generator.QAGenerator(retriever,llm)
    return chat_response_generator
def get_confluence_qa_response_generator():
    llm=llmintf.LLMIntf(llm_name="llama3")
    embedding=HuggingFaceEmbeddings()
    text_splitter=SemanticChunker(HuggingFaceEmbeddings())
    retriever=confluence_retriever.ConfluenceRetriever(embedding,text_splitter)
    #retriever.process_data_with_url("confluence site","access token","confluence space") - Replace with actual details
    chat_response_generator=qa_generator.QAGenerator(retriever,llm)
    return chat_response_generator


def main():
    chat_response_generator=get_pdf_qa_response_generator()
    #run streamlit
    st.set_page_config(page_title="RAG Demo", page_icon="💬")
    st.title("Chat bot using llama3 with few shot training")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history=[
            AIMessage(content="How can i help you...")
        ]
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                 st.write(message.content)

# user input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        with st.chat_message("Human"):
            st.markdown(user_query)
        with st.chat_message("AI"):
            response = chat_response_generator.generate_response(user_query, st.session_state.chat_history)
            st.write(response)
            st.session_state.chat_history.append(AIMessage(content=response))


if __name__=="__main__":
    main()
