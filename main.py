import os
from pathlib import Path, WindowsPath
from glob import glob
from shutil import move

path = Path(r"C:\Users\joaom\Downloads").glob("./*")
files = [file for file in path if file.is_file()]


to_file = {
    # Images
    "png": "Image",
    "jpg": "Image",
    "jpeg": "Image",
    "gif": "Image",
    "bmp": "Image",
    "tiff": "Image",
    "svg": "Image",
    "ico": "Image",
    "webp": "Image",
    # Audio
    "mp3": "Audio",
    "wav": "Audio",
    "ogg": "Audio",
    "wma": "Audio",
    "flac": "Audio",
    "aac": "Audio",
    "m4a": "Audio",
    # Video
    "mp4": "Video",
    "avi": "Video",
    "mkv": "Video",
    "mov": "Video",
    "wmv": "Video",
    "flv": "Video",
    "webm": "Video",
    "3gp": "Video",
    # Archives
    "rar": "Archive",
    "zip": "Archive",
    "7z": "Archive",
    "tar": "Archive",
    "gz": "Archive",
    "bz2": "Archive",
    "xz": "Archive",
    # Executables
    "exe": "Executable",
    "msi": "Executable",
    # Documents
    "csv": "Document",
    "json": "Document",
    "xml": "Document",
    "pdf": "Document",
    "doc": "Document",
    "docx": "Document",
    "xls": "Document",
    "xlsx": "Document",
    "ppt": "Document",
    "pptx": "Document",
    "txt": "Document",
    "rtf": "Document",
    "log": "Document",
    "md": "Document",
    "html": "Document",
    "htm": "Document",
    # Code
    "js": "Code",
    "py": "Code",
    "java": "Code",
    "c": "Code",
    "cpp": "Code",
    "h": "Code",
    "sql": "Code",
    "php": "Code",
    "asp": "Code",
    "jsp": "Code",
    "bat": "Code",
    "sh": "Code",
    "css": "Code",
    "xml": "Code",
    "ini": "Code",
    "cfg": "Code",
    # Fonts
    "ttf": "Font",
    "otf": "Font",
    "woff": "Font",
    "woff2": "Font",
    # Compressed
    "gz": "Compressed",
    "bz2": "Compressed",
    "xz": "Compressed",
    "z": "Compressed",
    # Database
    "sqlite": "Database",
    "db": "Database",
    # Miscellaneous
    "dat": "Miscellaneous",
    "conf": "Miscellaneous",
    "dll": "Miscellaneous",
    "iso": "Miscellaneous",
    "bin": "Miscellaneous",
    "pdb": "Miscellaneous",
    "rpm": "Miscellaneous",
    "deb": "Miscellaneous",
}


def mv_to_folder(file: WindowsPath) -> None:
    file_type = to_file[file.suffix[1::]]
    final_path = file.parent.joinpath(file_type)
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    move(file, final_path.joinpath(file.name))
    print(f"Moved {file} to {final_path.joinpath(file_type)}.")


with open("files.txt", "w") as f:
    for file in files:
        file_type = to_file[file.suffix[1::]]
        f.write(
            f'Path: "{file}", Suffix: {file.suffix}, Type: {file_type}, Parent: {file.parent}, File name: {file.name}\n'
        )


print(files)
for file in files:
    if file in 
    mv_to_folder(files)
