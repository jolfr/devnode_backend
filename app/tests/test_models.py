from django.test import TestCase
from app.models import Topic, Entry
from django.utils import timezone


# models test
class TopicTest(TestCase):

    def create_topic(self, text="title"):
        return Topic.objects.create(text=text, date_added = timezone.now())

    def test_topic_creation(self):
        t = self.create_topic()
        self.assertTrue(isinstance(t, Topic))
        self.assertEqual(t.__str__(), t.text)


class EntryTest(TestCase):

    def create_topic(self, text="title"):
        return Topic.objects.create(text=text, date_added=timezone.now())

    def create_entry(self, topic, text="entry"):
        return Entry.objects.create(topic=topic, text=text, date_added=timezone.now())

    def test_entry_creation(self):
        t = self.create_topic()
        e = self.create_entry(t)
        self.assertTrue(isinstance(e, Entry))
        self.assertEqual(e.topic, t)
        self.assertEqual(e.__str__(), e.text[:50] + "...")
