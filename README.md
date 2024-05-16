# RAG demo using Langchain , FAISS, LLAMA3 and Streamlit
## Introduction 
The application illustrates use of Langchain retrievers, generators and prompt templates to create a RAG pipeline
LLAMA3 8B is used as the LLM to process the input query 
## Design
The code is structured into 4 components :
1. *App/The driver code* : Has the streamlit calls, along with instantiation of other components. The chat history is also preserved here in memory
2. *The Retriever* : This creates the loader for various input formats such as documents,confluence, webpages etc converts the doccuments into word embeddings and then stores the same in a vector database
   for quick retrieval
4. *Generator* : The generator is reponsible for creating the prompt using the chat history, query and data from retriever.
5. *LLM interface* * : Currently kept in the most basic format , this will house the LLM APIs, access tokens etc.

## How to use 
1. pip install -r requirements.txt
2. streamlit run app.py

## Authors

Ankur Neog /ankurneog@outlook.com
