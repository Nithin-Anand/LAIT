"""Class to load prompt template. Designed for forward compatibility if storage format of prompt changes."""


_BASE_PROMPT = """I am asking you to analyse the following image, and create up to {max_keywords} appropriate keywords for this image. If necessary, think and then pick the best
keywords.  
The keywords will be embedded in the image metadata. Make sure the keywords are capitalised (not fully upper-case). Please return just the keywords as a comma-separated list.
Favour {tag_style} keywords.
"""

_DEBUG_PROMPT = """I am asking you to analyse the following image, and create up to {max_keywords} appropriate keywords for this image. If necessary, think and then pick the best
keywords.  
The keywords will be embedded in the image metadata. Please describe what you see in the image, followed by the keywords.
Favour {tag_style} keywords. """

def load_prompt_template() -> str:
    return _BASE_PROMPT

def load_debug_template() -> str:
    return _DEBUG_PROMPT