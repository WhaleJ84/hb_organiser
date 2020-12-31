from unittest import TestCase

from check import *


class HBOrganiserTestCase(TestCase):
    # === [ check_source_exists ] === #
    def test_check_source_exists_returns_false_on_empty_path(self):
        self.assertFalse(source_exists(''))

    def test_check_source_exists_returns_false_on_relative_bad_path(self):
        self.assertFalse(source_exists('~/fake_dir/'))

    def test_check_source_exists_returns_false_on_absolute_bad_path(self):
        self.assertFalse(source_exists('/home/fake_user/fake_dir/'))

    def test_check_source_exists_returns_true_on_relative_good_path(self):
        self.assertTrue(source_exists('library/'))

    def test_check_source_exists_returns_true_on_absolute_good_path(self):
        self.assertTrue(source_exists('/'))

    # === [ check_source_levels ] === #
    def test_check_source_levels_returns_false_on_no_platform(self):
        self.assertFalse(source_levels('library/bundle/'))

    def test_check_source_levels_returns_false_on_no_item(self):
        self.assertFalse(source_levels('library/bundle/item/'))

    def test_check_source_levels_returns_false_on_no_bundle(self):
        self.assertFalse(source_levels('library/bundle/item/platform/'))

    def test_check_source_levels_return_true_on_good_path(self):
        self.assertTrue('library/')
