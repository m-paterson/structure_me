#!/usr/bin/env python3
"""Functions module to hold the functions for folder and file creation from the
main program."""

import os


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
