import unittest

from ..answers_to_markdown import answers_to_markdown


class AnswersToMarkdownTestCase(unittest.TestCase):
    def test_it_should_transform_answers_into_markdown(self):
        answers = {
            'project_name': 'Project Name',
            'description': 'Description',
        }
        expected_markdown = """# Project Name
> Description
## Development Setup
```sh
#TODO
```
## Running Tests
```sh
#TODO
```
## Deployment
```sh
#TODO
```"""
        self.assertEqual(answers_to_markdown(answers), expected_markdown)
