class Generator:
    def __init__(self,retriever,llminterface,name):
        self.retriever=retriever
        self.llmintf=llminterface
        self.name=name