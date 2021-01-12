from os.path import abspath
from unittest import TestCase

from hb_organiser.cli import cli, verify_args


class HBOrganiserCliTesCase(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_verify_args_returns_true_on_good_relative_source_path_with_trailing_forward_slash(self):
        arguments = cli(['-s', 'tests/test_libraries/library/', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[0])

    def test_verify_args_returns_true_on_good_absolute_source_path_with_trailing_forward_slash(self):
        arguments = cli(['-s', abspath('tests/test_libraries/library/'), 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[0])

    def test_verify_args_returns_true_on_good_relative_source_path_without_trailing_forward_slash(self):
        arguments = cli(['-s', 'tests/test_libraries/library', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[0])

    def test_verify_args_returns_true_on_good_absolute_source_path_without_trailing_forward_slash(self):
        arguments = cli(['-s', abspath('tests/test_libraries/library'), 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[0])

    def test_verify_args_returns_none_on_source_bad_path(self):
        arguments = cli(['-s', 'tests/test_libraries/fake_library', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertIsNone(self, result[0])

    def test_verify_args_returns_true_on_good_relative_destination_path_with_trailing_forward_slash(self):
        arguments = cli(['-s', 'tests/test_libraries/library/', '-d', 'tests/test_destination/', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[1])

    def test_verify_args_returns_true_on_good_absolute_destination_path_with_trailing_forward_slash(self):
        arguments = cli(['-s', 'tests/test_libraries/library/', '-d', abspath('tests/test_destination/'), 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[1])

    def test_verify_args_returns_true_on_good_relative_destination_path_without_trailing_forward_slash(self):
        arguments = cli(['-s', 'tests/test_libraries/library/', '-d', 'tests/test_destination', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[1])

    def test_verify_args_returns_true_on_good_absolute_destination_path_without_trailing_forward_slash(self):
        arguments = cli(['-s', 'tests/test_libraries/library/', '-d', abspath('tests/test_destination'), 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertTrue(self, result[1])

    def test_dry_run_flag_overwrites_destination_flag_to_none(self):
        arguments = cli(['-s', 'tests/test_libraries/library', '-d', 'tests/test_destination', '-D', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertIsNone(self, result[1])

    def test_verify_args_returns_source_on_good_config_path(self):
        arguments = cli(['-c' 'tests/test.conf', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertEqual(self, result[0], 'tests/test_libraries/library')

    def test_verify_args_return_destination_on_good_config_path(self):
        arguments = cli(['-c', 'tests/test.conf', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertEqual(self, result[1], 'tests/test_destination')

    def test_verify_args_overwrites_config_source_on_set_source_flag(self):
        arguments = cli(['-c', 'tests/test.conf', '-s', 'tests/test_destination', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertEqual(self, result[0], 'tests/test_destination')

    def test_verify_args_overwrites_config_destination_on_set_destination_flag(self):
        arguments = cli(['-c', 'tests/test.conf', '-d', 'tests/test_libraries/library', 'all'])
        result = verify_args(arguments)
        HBOrganiserCliTesCase.assertEqual(self, result[1], 'tests/test_libraries/library')
