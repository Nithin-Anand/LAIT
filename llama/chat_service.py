from ollama_python import chat, ChatResponse

class LlamaChatService:

    def __init__(self, model: str):
        self.model = model

    def queryModel(self, prompt: str) -> ChatResponse:
        return self.model.chat(
            {
                "content": prompt
            }
        )
        
        