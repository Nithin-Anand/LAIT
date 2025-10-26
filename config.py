from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    MODEL: str = 'gemma3:4b-it-qat'

settings = Settings()