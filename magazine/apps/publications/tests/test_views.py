import io

from django.core.files.images import ImageFile
from django.test import TestCase
from django.urls import reverse

from apps.publications.models import Publication


class PublicationTestView(TestCase):

    def test_request(self):
        response = self.client.get(reverse('publication-list-url'))
        self.assertEqual(response.status_code, 200)


    def test_publication_detail_view(self):
        # local_file=open('test-image')
        temporary_image = ImageFile(io.BytesIO(b'some-file'),name='foo.jpd')
        pub=Publication.objects.create(title='some', description='desk',poster=temporary_image)
        url = reverse('publication-detail-url', kwargs={'pub_pk': pub.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_mistake(self):
        url= reverse('publication-detail-url',kwargs={'pub_pk':1})




