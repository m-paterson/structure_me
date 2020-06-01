#!/usr/bin/env python3
import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', 
        '--verbose', 
        help='include tips and directions on files. If no argument is passed, the'
             ' program will create a similar structure but the files will not '
             'contain any text.',
        action='store_true',
    )

    parser.add_argument(
        '-n',
        '--name',
        help='project name',
    )

    args = parser.parse_args()
    
    current_pwd = os.getcwd()
    project_folder = os.path.join(current_pwd, args.name)
    project_name = args.name
    
    folder_list = [
        project_folder, 
        'examples', 
        'src', 
        f'src/{project_name}', 
        'tests',
        'data',
    ]

    file_list = [
        'README.md',
        'setup.py',
        'setup.cfg',
        'MANIFEST.in',
        'examples/example.py',
        'src/__init__.py',
        '__init__.py',
    ]

    if args.verbose:
        print(f'verbose structure {project_name}')
    else:
        if os.path.exists(project_folder):
            print(f'{project_folder} already exists. Please specify a target that'
                   ' does not exist.')
        else:
            print(f'creating {project_folder}...')
            create_dirs(folder_list, project_name)
            create_files(project_folder, file_list, verbose=False)


def create_dirs(folder_list, project_name):
    '''Create folder structure.
    
    Args:
        folder_list: list. project folder list defined in main.
        project_name: str. project name passed as argument when invoking the main
            function.

    Returns:
        nothing.
    '''
    try:
        os.mkdir(folder_list[0])
        for folder in folder_list[1:]:
            os.mkdir(os.path.join(folder_list[0], folder))
    except FileExistsError as e:
        print('The destination folder already exists.', file=sys.stderr)
        raise


def create_files(root_folder, file_list, verbose=False):
    '''Create boilerplate files.

    Args:
        root_folder: str. project root folder.
        file_list: list. 
        verbose: bool. whether or not to add tips/comments to files.

    Returns:
        nothing.
    '''
    if verbose:
        print('verbose')
    else:
        try:
            for file in file_list:
                with open(os.path.join(root_folder, file), 'w'):
                    pass
        except FileExistsError as e:
            print('The destination folder already contain files. Specify an empty '
                  'location.', file=sys.stderr)
            raise


if __name__ == "__main__":
    main()