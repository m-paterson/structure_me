"""main function tests"""

import os

from structure_me.helper_functions import app_folders, parse_inputs
from structure_me.structure_me import main

from .test_base import TestBaseCase


class TestMainFunction(TestBaseCase):
    def test_structure_me_works_with_no_args(self):
        cwd = os.getcwd()
        os.chdir(self.tmp_dir.name)
        args = ["-n", "test_app"]
        main(args)
        root_folder = os.path.join(self.tmp_dir.name, "test_app")
        folder_tree = [x[0] for x in os.walk(root_folder)]
        folders_list = app_folders("test_app")
        try:
            for folder in folders_list:
                folder = os.path.abspath(os.path.join(root_folder, folder))
                self.assertTrue(folder in folder_tree)
        finally:
            os.chdir(cwd)

        # os.system('python structure_me/src/structure_me/structure_me.py')
