from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import os
from pathlib import Path, WindowsPath
from glob import glob
from shutil import move
from file_types import to_file


def mv_to_folder(path) -> None:
    file = Path(path)
    if file.suffix[1::].lower() not in to_file.keys():
        print(f"{file.suffix[1::].lower()} is not an accepted file extension.")
        return
    file_type = to_file[file.suffix[1::]]
    final_path = file.parent.joinpath(file_type)
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    move(file, final_path.joinpath(file.name))
    print(f"Moved {file} to {final_path.joinpath(file.name)}.")


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"Watchdog detected change: {event.src_path}")
        mv_to_folder(event.src_path)


def watch_directory(directory_path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()
    print(f"Watching directory: {directory_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    path = Path(r"C:\Users\joaom\Downloads")
    files_path = path.glob("./*")
    files = [file for file in files_path if file.is_file()]

    """with open("files.txt", "w", encoding="utf-8") as f:
        for file in files:
            file_type = to_file[file.suffix[1::].lower()]
            f.write(
                f'Path: "{file}", Suffix: {file.suffix}, Type: {file_type}, Parent: {file.parent}, File name: {file.name}\n'
            )"""
    for file in files:
        if file.suffix[1::] not in to_file.keys():
            print(f"{file.suffix[1::]} is not an accepted file extension.")
            continue
        file_type = to_file[file.suffix[1::]]
        final_path = file.parent.joinpath(file_type)
        if not os.path.exists(final_path):
            os.makedirs(final_path)
        move(file, final_path.joinpath(file.name))
        print(f"Moved {file} to {final_path.joinpath(file.name)}.")

    # print(files)
    directory_to_watch = path
    watch_directory(directory_to_watch)
