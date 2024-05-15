import os
from langchain_community.document_loaders import PyPDFLoader
from .retriever_base import Retriever
class PDFRetriever(Retriever):
    def __init__(self,embedding,splitter):
        super().__init__(embedding,splitter,"PDFRetriever")
    def process_data_with_directory(self,path_to_files):
        documents = []
        for file in os.listdir(path_to_files):
            if file.endswith('.pdf'):
                pdf_path_with_filename = os.path.join(path_to_files, file)
                loader = PyPDFLoader(pdf_path_with_filename)
                documents.extend(loader.load())
        self.create_vector_db(documents)