from pathlib import Path
from file_extensions import FILE_EXTENSIONS


def read_image_files(folder_path: Path) -> list[Path]:

    all_files = folder_path.glob("**/*")

    image_files = [file for file in all_files if file.is_file() and file.name.lower().split(".")[-1] in FILE_EXTENSIONS]
    
    return image_files
    
test_path = Path("/Users/nithinanand/Pictures/Photos/Fujifilm X100F/2025/09/Two Months of Photos/Two Months of Photos_jpg")