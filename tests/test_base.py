"""base class for unit testing structure_me"""

import tempfile
import unittest


class TestBaseCase(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp_dir.cleanup()
