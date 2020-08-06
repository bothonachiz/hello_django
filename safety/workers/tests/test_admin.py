from django.test import TestCase
from django.contrib import admin
from ..models import Worker
from ..admin import WorkerAdmin


class TestWorkerAdmin(TestCase):
    def test_admin_should_be_register(self):
         self.assertTrue(isinstance(admin.site._registry[Worker], WorkerAdmin))

    def test_admin_should_set_list_disaplay(self):
        # Given
        expected = (
            'first_name',
            'last_name',
            'is_available',
            'primary_phone',
            'secondary_phone',
            'address',
        )

        # When
        # Create list diaplay in ..admin

        # Then
        self.assertEqual(WorkerAdmin.list_display, expected)

    def test_admin_should_set_list_filter(self):
        # Given
        expected = (
            'is_available',
        )

        # When
        # Create list filter in ..admin

        # Then
        self.assertEqual(WorkerAdmin.list_filter, expected)
        