from django.test import TestCase
from ..models import Worker


class TestWorker(TestCase):
    def test_worker_shoud_have_defined_fields(self):
        # Given
        first_name = 'Narongvit'
        last_name = 'Promkhana'
        is_available = True
        primary_phone = '087-784-878x'
        secondary_phone = '082-524-818x'
        address = 'Geeky Base All Star'

        # When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )

        # Then
        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertTrue(worker.is_available)
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)
