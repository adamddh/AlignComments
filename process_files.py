"""
Formats all Javascript docstrings in a directory to be compatible with JSDoc.
"""

import os
import sys


def process_file(file_path):
    """
    Processes a file to be compatible with JSDoc.


    Parameters
    ----------
    file_path : str
        The path to the file to be processed.
    """
    with open(file_path, "r", encoding="utf-8") as fin:
        content = fin.readlines()

    modified_content = []
    javadoc_started = False
    indent = ""

    for line in content:
        if line.strip().startswith("/*"):
            javadoc_started = True
            modified_content.append(line)
            indent = line.split("/*")[0]
        elif javadoc_started and line.strip().startswith("*/"):
            javadoc_started = False
            modified_content.append(line)
        elif javadoc_started and line.strip().startswith("*"):
            modified_content.append(
                f"{indent} " + line.lstrip("*").strip() + "\n")
        else:
            modified_content.append(line)

    with open(file_path, "w", encoding="utf-8") as fout:
        fout.write("".join(modified_content))


def process_directory(dir_path):
    """
    Processes a directory to be compatible with JSDoc.

    Parameters
    ----------
    dir_path : str
        The path to the directory to be processed.
    """
    for item in os.listdir(dir_path):
        item: str
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            process_directory(item_path)
        elif os.path.isfile(item_path) and item.endswith(".js"):
            process_file(item_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a directory path as a command line argument.")
        sys.exit(1)

    DIRECTORY_PATH = sys.argv[1]

    process_directory(DIRECTORY_PATH)
