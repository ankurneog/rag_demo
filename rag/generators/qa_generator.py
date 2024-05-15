from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from .generator_base import Generator
#import retrievers
#import language_models

class QAGenerator(Generator) :
    def __init__(self,retriever,llmintf):
        super().__init__(retriever,llmintf,"QAGenerator")
        print("Creating Question Answer Generator")
    def generate_response(self,user_query,chat_history):
           #langchain prompt template
        template = """
            You are a helpful assistant. Answer the following questions considering the history of the conversation:
            Context : {context}
            User question: {question}
            Helpful Answer:
            """
        QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
        qa_chain = RetrievalQA.from_chain_type(
                        self.llmintf.get_llm(),
                        retriever=self.retriever.get_retriever(),
                        return_source_documents=True,
                        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
                    )
        results=qa_chain({"query":user_query,"context":"chat_history"})
        response = str(results["result"])
        print(response)
        return response
    
