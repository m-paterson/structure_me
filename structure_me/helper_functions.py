#!/usr/bin/env python3
"""Functions module to hold the functions for folder and file creation from the
main program."""

import argparse
import os


def parse_inputs(args):
    """parse arguments passed when running the script
    Args:
        None

    Returns:
        parsed arguments
    """
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
        "-n",
        "--name",
        help="project name, used to create the folder name. ideally no "
        "spaces or funny characters should be passed or it might raise "
        "and exception.",
        action="store",
        required=True,
    )

    return parser.parse_args(args)


def create_folder(root_folder, folder_name):
    """Create a folder inside root folder.
    Args:

        root_folder (str): target location for your app.
        folder_name (str): folder name you want to create.

    Returns:

        Nothing

    example:
    >>> create_folder('C:/temp', 'test_app')
    >>> os.path.exists('C:/temp/test_app')
        True
    """
    try:
        target_folder = os.path.join(root_folder, folder_name)
        os.makedirs(target_folder, exist_ok=True)
    except Exception as e:
        print(f"Could not create forder {target_folder}.")
        raise e


def create_file(root_folder, app_name, file, use_template=False):
    """Create a file in the specified target.
    Args:

        root_folder (str): project root folder.
        app_name (str): project name.
        file (str): file to be created.
        use_template (bool, optional): whether or not to use the templates

    Returns:

        Nothing.

    >>> create_file('C:/temp', 'test_app', 'README.md')
    >>> os.path.exists('C:/temp/test_app/README.md')
        True
    """
    full_file_path = os.path.join(root_folder, app_name, file)
    content = ""
    if use_template:
        if file in ["README.md", "setup.cfg", "setup.py"]:
            template_folder = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__))
            )
            try:
                with open(
                    os.path.join(template_folder, f"data/sample_{file}"),
                    "r",
                    encoding="utf-8",
                ) as sample:
                    content = sample.read()
            except Exception as e:
                print(f"Error reading template sample_{file}")
                raise e
    try:
        with open(full_file_path, "w", encoding="utf-8") as new_file:
            new_file.writelines(content)
    except Exception as e:
        print(f"Could not create file {full_file_path}.")
        raise e


def app_folders(proj_name):
    """Create a list with the project folder tree
    Args:
        proj_name (str): the name of the project, where the code will be hosted

    Returns:
        folder_list (list): list containing the main folder tree
    """
    folders_list = [
        f"{proj_name}",
        f"{proj_name}/data",
        "tests",
    ]
    return folders_list


def app_files(proj_name):
    """Create a list with the project files
    Args:
        proj_name (str): the name of the project, where the code will be hosted

    Returns:
        files_list (list): list containing the file structure of the app
    """
    files_list = [
        "README.md",
        "setup.py",
        "setup.cfg",
        f"{proj_name}/__init__.py",
        f"{proj_name}/{proj_name}.py",
        "tests/tests.py",
    ]
    return files_list
