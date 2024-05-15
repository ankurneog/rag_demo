from langchain_community.llms import Ollama
class LLMIntf :
    def __init__(self,llm_name="llama3"):
        self.llm =Ollama(model=llm_name)
        self.llm_name=llm_name
    def get_llm(self):
        return self.llm
    def get_llm_name(self):
        return self.llm_name

