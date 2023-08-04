from .py_generate import PyGenerator
from .rs_generate import RsGenerator
from .generator_types import Generator

def generator_factory(lang: str) -> Generator:
    if lang in {"py", "python"}:
        return PyGenerator()
    elif lang in {"rs", "rust"}:
        return RsGenerator()
    else:
        raise ValueError(f"Invalid language for generator: {lang}")
