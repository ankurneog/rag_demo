import os
from langchain_community.vectorstores import FAISS


class Retriever:
    def __init__(self,embedding,splitter,name):
        self.embedding=embedding
        self.splitter=splitter
        self.name=name
    def create_vector_db(self,documents):
        documents_chunks=self.splitter.split_documents(documents)
        self.vectordb = FAISS.from_documents(documents_chunks, self.embedding)
    def save_db(self,path):
        self.vectordb.save_local(path)
    def get_retriever(self):
        #https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/
        return self.vectordb.as_retriever()
    def get_data_from_query(self,query):
        return self.vectordb.similarity_search(query)
    def load_stored_db(self,path_to_db):
        if(os.path.exists(path_to_db)):
            self.vectordb=FAISS.load_local("faiss_index", self.embeddings)
        else:
            print("Db not found in path : ", path_to_db)
            return False
        return True