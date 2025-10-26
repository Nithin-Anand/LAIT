from pathlib import Path
from file_extensions import FILE_EXTENSIONS


def read_image_files(folder_path: Path) -> list[Path]:
    all_files = folder_path.glob("**/*")

    image_files = [
        file
        for file in all_files
        if file.is_file() and file.name.lower().split(".")[-1] in FILE_EXTENSIONS
    ]

    return image_files
