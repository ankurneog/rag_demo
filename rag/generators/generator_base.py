class Generator:
    def __init__(self,retriever,llm,name):
        self.retriever=retriever
        self.llmintf = llm
        self.name=name