from langchain_community.document_loaders import ConfluenceLoader
from  .retriever_base import Retriever

class ConfluenceRetriever(Retriever):
    def __init__(self,embedding,splitter):
        super().__init__(embedding,splitter,"ConfluenceRetriever")
    def process_data_with_url(self,url,access_token,space_id):
       loader = ConfluenceLoader(url=url, token=access_token,max_pages=50,limit=50,include_attachments=True,space_key=space_id)
       documents = loader.load()
       self.create_vector_db(documents)