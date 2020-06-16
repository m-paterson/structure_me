#!/usr/bin/env python3
import argparse
import os
import sys

current_dir = os.getcwd()
project_name = 'project_name'
root_folder = os.path.join(current_dir, project_name)

folders_list = [
        "examples",
        "src",
        f"src/{project_name}",
        f"src/{project_name}/data",
        "tests",
]

files_list = [
        "README.md",
        "setup.py",
        "setup.cfg",
        "examples/example.py",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/{project_name}.py",
        "tests/tests.py",
]