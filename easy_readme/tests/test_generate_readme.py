import unittest

from ..defaults import get_default_project_name


class GetDefaultProjectNameTestCase(unittest.TestCase):
    def test_it_should_default_to_title_cased_directory_name(self):
        self.assertEqual(get_default_project_name('/foo-bar'), 'Foo Bar')

    def test_it_should_handle_underscore_separated_name(self):
        self.assertEqual(get_default_project_name('/foo_bar'), 'Foo Bar')
