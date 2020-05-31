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

    if args.verbose:
        print(f'verbose structure {project_name}')
    else:
        if os.path.exists(project_folder):
            print(f'{project_folder} already exists. Please specify a target that'
                   ' does not exist.')
        else:
            print(f'creating {project_folder}...')
            create_dirs(project_folder, project_name)
            create_files(project_folder, project_name, verbose=False)


def create_dirs(root_folder, project_name):
    '''Create folder structure.
    
    Args:
        root_folder: str. root project folder passed as argument to the main script.

    Returns:
        nothing.
    '''
    try:
        folder_list = ['examples', 'src', f'src/{project_name}', 'tests', 'data']
        os.mkdir(root_folder)
        for folder in folder_list:
            os.mkdir(os.path.join(root_folder, folder))
    except FileExistsError as e:
        print('The destination folder already exists.', file=sys.stderr)
        raise


def create_files(root_folder, project_name, verbose=False):
    '''Create boilerplate files.

    Args:
        root_folder: str. root project folder passed as argument to the main script.
        verbose: bool. whether or not to add tips/comments to files.

    Returns:
        nothing.
    '''
    if verbose:
        print('verbose')
    else:
        try:
            examples_folder = os.path.join(root_folder, 'examples')
            src_folder = os.path.join(root_folder, f'src\{project_name}')
            test_folder = os.path.join(root_folder, 'tests')
            file_list = [
                os.path.join(root_folder, 'README.MD'),
                os.path.join(root_folder, 'setup.py'),
                os.path.join(examples_folder, 'example.py'),
                os.path.join(src_folder, '__init__.py'),
                os.path.join(test_folder, '__init__.py'),
            ]
            for file in file_list:
                with open(file, 'w'):
                    pass

        except FileExistsError as e:
            print('The destination folder already contain files. Specify an empty '
                  'location.', file=sys.stderr)
            raise


if __name__ == "__main__":
    main()