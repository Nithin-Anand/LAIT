import os
from config import model_settings
from loguru import logger

class ModelDeploymentService:
    def __init__(self):
        self.model = model_settings.model
        self.deployed = False

    def run_model(self) -> None:
        if self.deployed:
            logger.info(f"Model {self.model} is already deployed")

        os.system(self.build_model_run_command)

        logger.info(f"Model {self.model} deployed")
        self.deployed = True

    def build_model_run_command(self):
        return f"ollama run {self.model}"
