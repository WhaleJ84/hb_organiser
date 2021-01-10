from os.path import abspath
from unittest import TestCase

from hb_organiser.cli import *


class HBOrganiserCliTesCase(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_verify_args_returns_true_on_good_relative_source_path_with_trailing_forward_slash(self):
        setup = cli(['-s', 'tests/test_libraries/library/', 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)

    def test_verify_args_returns_true_on_good_absolute_source_path_with_trailing_forward_slash(self):
        setup = cli(['-s', abspath('tests/test_libraries/library/'), 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)

    def test_verify_args_returns_true_on_good_relative_source_path_without_trailing_forward_slash(self):
        setup = cli(['-s', 'tests/test_libraries/library', 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)

    def test_verify_args_returns_true_on_good_absolute_source_path_without_trailing_forward_slash(self):
        setup = cli(['-s', abspath('tests/test_libraries/library'), 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)

    def test_verify_args_returns_false_on_source_bad_path(self):
        setup = cli(['-s', 'tests/test_libraries/fake_library', 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertFalse(self, result)

    def test_verify_args_returns_true_on_good_relative_destination_path_with_trailing_forward_slash(self):
        setup = cli(['-s', 'tests/test_libraries/library/', '-d', 'tests/test_destination/', 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)

    def test_verify_args_returns_true_on_good_absolute_destination_path_with_trailing_forward_slash(self):
        setup = cli(['-s', 'tests/test_libraries/library/', '-d', abspath('tests/test_destination/'), 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)

    def test_verify_args_returns_true_on_good_relative_destination_path_without_trailing_forward_slash(self):
        setup = cli(['-s', 'tests/test_libraries/library/', '-d', 'tests/test_destination', 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)

    def test_verify_args_returns_true_on_good_absolute_destination_path_without_trailing_forward_slash(self):
        setup = cli(['-s', 'tests/test_libraries/library/', '-d', abspath('tests/test_destination'), 'all'])
        result = verify_args(setup)
        HBOrganiserCliTesCase.assertTrue(self, result)
