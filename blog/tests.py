from django.test import TestCase
from .models import *


#                                      TESTING MODELS
class PostsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Posts.objects.create(title='Как найти первую работу аниматором?')

    def test_title_label(self):
        my_post = Posts.objects.get(id=1)
        field_label = my_post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        my_post = Posts.objects.get(id=1)
        max_length = my_post._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_post_name(self):
        my_post = Posts.objects.get(id=1)
        expected_object_name = f'{my_post.title}'
        self.assertEqual(str(my_post), expected_object_name)


class AboutSiteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        AboutSite.objects.create(title='Зачем нужен этот блог?')

    def test_title_label(self):
        content = AboutSite.objects.get(id=1)
        field_label = content._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        content = AboutSite.objects.get(id=1)
        max_length = content._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_phone_max_length(self):
        content = AboutSite.objects.get(id=1)
        max_length = content._meta.get_field('my_phone').max_length
        self.assertEqual(max_length, 13)

    def test_mail_max_length(self):
        content = AboutSite.objects.get(id=1)
        max_length = content._meta.get_field('my_mail').max_length
        self.assertEqual(max_length, 30)

    def test_facebook_max_length(self):
        content = AboutSite.objects.get(id=1)
        max_length = content._meta.get_field('facebook_link').max_length
        self.assertEqual(max_length, 100)

    def test_instagram_max_length(self):
        content = AboutSite.objects.get(id=1)
        max_length = content._meta.get_field('instagram_link').max_length
        self.assertEqual(max_length, 100)

    def test_youtube_max_length(self):
        content = AboutSite.objects.get(id=1)
        max_length = content._meta.get_field('youtube_link').max_length
        self.assertEqual(max_length, 100)

    def test_linkedn_max_length(self):
        content = AboutSite.objects.get(id=1)
        max_length = content._meta.get_field('linkedn_link').max_length
        self.assertEqual(max_length, 100)


class MainPageTextModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MainPageText.objects.create(title='Если ты еще сомневаешься...')

    def test_title_label(self):
        main_page_content = MainPageText.objects.get(id=1)
        field_label = main_page_content._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_linkedn_max_length(self):
        main_page_content = MainPageText.objects.get(id=1)
        max_length = main_page_content._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)


class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        City.objects.create(title='Анталия. Отели, специфика работы, природа и климат.')

    def test_title_label(self):
        city_content = City.objects.get(id=1)
        field_label = city_content._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        city_content = City.objects.get(id=1)
        max_length = city_content._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)


class SponsorshipModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Sponsorship.objects.create(title='Хочешь поддержать проект?')

    def test_title_label(self):
        sponsor = Sponsorship.objects.get(id=1)
        field_label = sponsor._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        sponsor = Sponsorship.objects.get(id=1)
        max_length = sponsor._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)