"""Testing for the Story class."""

from models.story import Story
from tests.test_configs.test_config1 import STORY_BLUEPRINTS
import unittest


class TestStoryClass(unittest.TestCase):

    def test_story_import(self):
        story = Story(STORY_BLUEPRINTS)
        self.assertTrue(story.chapters[1])

    def test_story_get(self):
        story = Story(STORY_BLUEPRINTS)
        self.assertEqual(story.get_chapter(1), 'I ran out of the house.')
