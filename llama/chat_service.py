from ollama import generate, ChatResponse


class OllamaGenerateService:
    def __init__(self, model: str):
        self.model = model

    def query_model(self, prompt: str, image_location: str) -> ChatResponse:
        return generate(model=self.model, prompt=prompt, images=[image_location])
