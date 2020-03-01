from config.story_blueprints import STORY_BLUEPRINTS


class Story:
    def __init__(self, STORY_BLUEPRINTS):
        self.chapters = [chapter for chapter in STORY_BLUEPRINTS]

    def get_chapter(self, chapter_num):
        return self.chapters[chapter_num - 1]
