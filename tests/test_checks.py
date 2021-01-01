from unittest import TestCase

from hb_organiser.check import *


class HBOrganiserTestCase(TestCase):
    # === [ source_exists ] === #
    def test_source_exists_returns_false_on_empty_path(self):
        self.assertFalse(source_exists(''))

    def test_source_exists_returns_false_on_relative_bad_path(self):
        self.assertFalse(source_exists('~/fake_dir/'))

    def test_source_exists_returns_false_on_absolute_bad_path(self):
        self.assertFalse(source_exists('/home/fake_user/fake_dir/'))

    def test_source_exists_returns_true_on_relative_good_path(self):
        self.assertTrue(source_exists('tests/test_libraries/library/'))

    def test_source_exists_returns_true_on_absolute_good_path(self):
        self.assertTrue(source_exists('/'))

    # === [ source_levels ] === #
    def test_source_levels_returns_false_on_no_platform(self):
        self.assertFalse(source_levels('tests/test_libraries/library/bundle/'))

    def test_source_levels_returns_false_on_no_item(self):
        self.assertFalse(source_levels('tests/test_libraries/library/bundle/item/'))

    def test_source_levels_returns_false_on_no_bundle(self):
        self.assertFalse(source_levels('tests/test_libraries/library/bundle/item/platform/'))

    def test_source_levels_return_true_on_good_path(self):
        self.assertTrue(source_levels('tests/test_libraries/library/'))

    def test_source_levels_return_true_when_target_set(self):
        self.assertTrue(source_levels('tests/test_libraries/library/', 'bundle'))

    # === [ number_of_items ] === #
    def test_number_of_items_returns_zero_ignoring_directories(self):
        self.assertEqual(number_of_items('tests/test_libraries/library/', ['all']), 1)

    def test_number_of_items_returns_one_ignoring_md5_and_directories(self):
        self.assertEqual(number_of_items('tests/test_libraries/other_library/', ['all']), 1)
