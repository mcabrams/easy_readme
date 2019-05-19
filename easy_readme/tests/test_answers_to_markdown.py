import unittest

from ..answers_to_markdown import answers_to_markdown


class AnswersToMarkdownTestCase(unittest.TestCase):
    def test_it_should_transform_project_name_into_markdown(self):
        answers = {
            'project_name': 'Project Name',
        }
        expected_markdown = """# Project Name"""
        self.assertEqual(answers_to_markdown(answers), expected_markdown)
