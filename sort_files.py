import argparse
from pathlib import Path
from shutil import copyfile
from concurrent.futures import ThreadPoolExecutor
import logging
from time import time
from uuid import uuid4

"""
python3 sort_files.py --source -s picture
python3 sort_files.py --output -o dest
"""
parser = argparse.ArgumentParser(description="App for sorting folder")
parser.add_argument("-s", "--source", help="Source folder", required=True)
parser.add_argument("-o", "--output", default="dest")
args = vars(parser.parse_args())  # object -> dict
source = args.get("source")
output = args.get("output")


folders = []


def grabs_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)


def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = output_folder.joinpath(ext)
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                if new_path.joinpath(el.name).exists():
                    copyfile(el, new_path.joinpath(f"{el.stem}_{uuid4()}{el.suffix}"))
                else:
                    copyfile(el, new_path.joinpath(el.name))
                logging.debug(f"File {el} copied to {new_path}")
            except OSError as e:
                logging.error(e)
    return "Ok"


if __name__ == "__main__":
    timer = time()
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    base_folder = Path(source)
    output_folder = Path(output)

    folders.append(base_folder)
    grabs_folder(base_folder)
    print(folders)

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(sort_file, folders))

    logging.debug(results)
    logging.debug(f"The program finished in {time() - timer} seconds")
    print(f"\nМожна видаляти початкову теку  {base_folder}")
