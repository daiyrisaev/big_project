from django.test import TestCase

# def calc_summa(a,b):
#     return a+b
#
# class TestExample(TestCase):
#
#     def test_first(self):
#         result = calc_summa(5, 15)
#         expected = 20
#         self.assertEqual(result, expected)
#
#     def test_second(self):
#         result = calc_summa(1, )
#         expected = 20
#         self.assertEqual(result, expected)
from apps.publications.models import PublicationCategory, Publication


class TestPublicationCategory(TestCase):

    def setUp(self) -> None:
        self.category=PublicationCategory.objects.create(title='общая категория')


    def test_create_category(self):
        cat1=PublicationCategory.objects.create(title='первая категория')
        self.assertEqual(cat1.title,'первая категория')


    def test_create_publication(self):
        publication1 = Publication.objects.create(title='публикация',description='описание',category=self.category)
        self.assertEqual(publication1.title,'публикация')
        self.assertEqual(publication1.description,'описание')
        self.assertEqual(publication1.category.id ,self.category.id)
        self.assertEqual(publication1.created.at,None)


