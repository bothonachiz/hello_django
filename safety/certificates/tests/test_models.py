from django.test import TestCase
from django.core.files import File

from ..models import Certificate


class TestCertificate(TestCase):
    def test_certificater_shoud_have_defined_fields(self):
        # Given
        name = 'Django Certificate by ODDS'
        issue_by = 'Proof'

        # When
        certificate = Certificate.objects.create(
            name=name,
            issue_by=issue_by
        )

        # Then
        assert certificate.name == name
        assert certificate.issue_by == issue_by
