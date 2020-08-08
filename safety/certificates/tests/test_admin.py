from django.test import TestCase
from django.contrib import admin

from ..models import Certificate
from ..admin import CertificateAdmin


class TestCertificateAdmin(TestCase):
    def test_admin_should_be_register(self):
        assert isinstance(
            admin.site._registry[Certificate], CertificateAdmin) is True

    def test_admin_should_set_list_disaplay(self):
        # Given
        expected = (
            'name',
            'issue_by',
        )

        # Then
        assert CertificateAdmin.list_display == expected
