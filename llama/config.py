from pydantic_settings import BaseSettings

class ModelSettings(BaseSettings):

    MODEL: str = 'gemma3:4b-it-qat'

model_settings = ModelSettings()