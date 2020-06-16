import os

from structure_me.src.structure_me.helper_functions import (create_file,
                                                            create_folder)
from structure_me.src.structure_me.structure_me import files_list

from .test_base import TestBaseCase


class TestFiles(TestBaseCase):
    def test_can_create_file(self):
        create_folder(self.tmp_dir.name, "test_app")
        create_file(self.tmp_dir.name, "test_app", "test_file.txt")
        self.assertTrue(
            os.path.exists(os.path.join(self.tmp_dir.name, "test_app/test_file.txt"))
        )

    def test_can_create_template_file(self):
        create_folder(self.tmp_dir.name, "test_app")
        create_file(self.tmp_dir.name, "test_app", "README.md", use_template=True)
        self.assertTrue(
            os.path.exists(os.path.join(self.tmp_dir.name, "test_app/README.md"))
        )
