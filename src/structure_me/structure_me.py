#!/usr/bin/env python3
import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        "--expressive",
        help="include tips and directions on files. If no argument is passed, the"
        " program will create a similar structure but the files will not "
        "contain any text.",
        action="store_true",
    )

    parser.add_argument(
        "-n", "--name", help="project name",
    )

    args = parser.parse_args()

    current_dir = os.getcwd()
    project_folder = os.path.join(current_dir, args.name)
    project_name = args.name

    folder_list = [
        project_folder,
        "examples",
        "src",
        f"src/{project_name}",
        f"src/{project_name}/data",
        "tests",
    ]

    file_list = [
        "README.md",
        "setup.py",
        "setup.cfg",
        "examples/example.py",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/{project_name}.py",
        "tests/tests.py",
    ]

    expressive = False
    if args.expressive:
        expressive = True
    try:
        create_dirs(folder_list, project_name)
        create_files(project_folder, file_list, expressive=expressive)
    except OSError as e:
        raise e


def create_dirs(folder_list, project_name):
    """Create folder structure.

    Args:
        folder_list: list. project folder list defined in main.
        project_name: str. project name passed as argument when invoking the main
            function.

    Returns:
        nothing.
    """
    try:
        os.mkdir(folder_list[0])
        for folder in folder_list[1:]:
            os.mkdir(os.path.join(folder_list[0], folder))
    except FileExistsError as e:
        print("The destination folder already exists.", file=sys.stderr)
        raise e


def create_files(root_folder, file_list, expressive=False):
    """Create boilerplate files.

    Args:
        root_folder: str. project root folder.
        file_list: list.
        expressive: bool. whether or not to add tips/comments to files.

    Returns:
        nothing.
    """
    _location = os.path.realpath(
        os.path.join(os.getcwd(),
        os.path.dirname(__file__))
    )
    if expressive:
        try:
            for file in file_list:
                content = ""
                if file in ["README.md", "setup.py", "setup.cfg"]:
                    with open(
                        os.path.join(_location, f"data/sample_{file}"),
                        "r",
                        encoding="utf-8",
                    ) as sample:
                        content = sample.read()
                with open(os.path.join(root_folder, file), "w") as target:
                    target.writelines(content)
        except FileExistsError as e:
            print(
                "It seems that some of the files already exist in the target location. "
                "Please specify and empty target location!"
            )
            raise e
    else:
        try:
            for file in file_list:
                with open(os.path.join(root_folder, file), "w"):
                    pass
        except FileExistsError as e:
            print(
                "The destination folder already contain files. Specify an empty "
                "location.",
                file=sys.stderr,
            )
            raise e


if __name__ == "__main__":
    main()
