from django.test import TestCase
from django.core.files import File

from ..models import Certificate
from workers.models import Worker


class TestCertificate(TestCase):
    def test_certificater_shoud_have_defined_fields(self):

        worker = Worker.objects.create(
            first_name='Narongvit',
            last_name='Promkhana',
            is_available=True,
            primary_phone='087-784-878x',
            secondary_phone='082-524-818x',
            address='Geeky Base All Star',
        )

        # Given
        name = 'Django Certificate by ODDS'
        issue_by = 'Proof'

        # When
        certificate = Certificate.objects.create(
            name=name,
            issue_by=issue_by,
            worker=worker
        )

        # Then
        assert certificate.name == name
        assert certificate.issue_by == issue_by
        assert certificate.worker.first_name == worker.first_name
