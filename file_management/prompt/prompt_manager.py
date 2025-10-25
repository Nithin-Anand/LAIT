from typing import Any

def format_prompt(prompt_template: str, prompt_parameters: dict[str, Any]) -> str:
    return prompt_template.format_map(prompt_parameters)