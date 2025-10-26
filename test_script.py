from llama import OllamaGenerateService, OllamaService
from prompt import load_prompt_template, load_debug_template, PromptBuilder
from loguru import logger
from config import settings


def test_workflow():
    deployment_service = OllamaService(initialisation_buffer=10)
    chat_service = OllamaGenerateService(settings.MODEL)
    prompt_template = load_prompt_template()
    prompt_builder = PromptBuilder(
        prompt_template=prompt_template,
        tag_style="broad, categorical, considering of mood",
    )

    deployment_service.start_ollama_server()

    test_image_location = "/Users/nithinanand/Documents/projects/LAIT/NITH7488.jpg"

    prompt = prompt_builder.build_prompt()
    logger.info(prompt)

    response = chat_service.query_model(
        prompt=prompt, image_location=test_image_location
    )

    logger.info(f"Model response: {response['response']}")

    deployment_service.stop_ollama_server()
