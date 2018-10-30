from django.test import TestCase
from app.models import Topic, Entry
from django.utils import timezone


# models test
class TopicTest(TestCase):

    @staticmethod
    def create_topic(text="title"):
        return Topic.objects.create(text=text, date_added = timezone.now())

    def test_topic_creation(self):
        t = self.create_topic()
        self.assertTrue(isinstance(t, Topic))
        self.assertEqual(t.__str__(), t.text)


class EntryTest(TestCase):

    @staticmethod
    def create_topic(text="title"):
        return Topic.objects.create(text=text, date_added=timezone.now())

    @staticmethod
    def create_entry(topic=create_topic(), text="entry"):
        return Entry.objects.create(topic=topic, text=text, date_added=timezone.now())

    def test_entry_creation(self):
        e = self.create_entry()
        self.assertTrue(isinstance(e, Entry))
