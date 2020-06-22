#!/usr/bin/env python3
"""Create a default project folder given arguments passed to the main function"""
import os
import sys

from .helper_functions import (
    create_file,
    create_folder,
    app_files,
    app_folders,
    parse_inputs,
)


def main(args=sys.argv[1:]):
    parser = parse_inputs(args)
    current_dir = os.getcwd()
    try:
        project_name = parser.name
    except Exception as e:
        print("Check that you have passed an app name to the script.")
        raise e

    folders_list = app_folders(project_name)

    files_list = app_files(project_name)

    expressive = False
    if parser.expressive:
        expressive = True

    # note makedirs, invoked in the create_folder function, create intermediary
    # folders if needed
    for folder in folders_list:
        create_folder(os.path.join(current_dir, project_name), folder)

    for file in files_list:
        create_file(current_dir, project_name, file, use_template=expressive)


if __name__ == "__main__":
    main()
