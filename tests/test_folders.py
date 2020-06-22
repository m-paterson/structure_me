import os

from structure_me.helper_functions import app_folders, create_folder

from .test_base import TestBaseCase


class TestFolders(TestBaseCase):
    def test_can_create_app_folder(self):
        create_folder(self.tmp_dir.name, "test_app")
        self.assertTrue(os.path.exists(os.path.join(self.tmp_dir.name, "test_app")))

    def test_can_create_project_folder(self):
        root_folder = os.path.join(self.tmp_dir.name, "test_app")
        folders_list = app_folders("test_app")
        for folder in folders_list:
            create_folder(root_folder, folder)
        folder_tree = [x[0] for x in os.walk(root_folder)]
        for folder in folders_list:
            folder = os.path.abspath(os.path.join(root_folder, folder))
            self.assertTrue(folder in folder_tree)
