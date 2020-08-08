from django.test import TestCase

from ..models import Certificate
from ..views import CertificateModelViewSetView
from ..serializers import CertificateModelSerializer


class TestCertificateModelViewSet(TestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get("/certificates/")
        assert response.status_code == 200

    def test_model_view_set_should_set_query_set(self):
        assert list(CertificateModelViewSetView.queryset) == list(
            Certificate.objects.all())
