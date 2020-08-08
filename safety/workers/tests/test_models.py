import os
from unittest.mock import MagicMock

from django.test import TestCase
from django.core.files import File

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

        # mock image
        image_profile = MagicMock(spec=File)
        image_profile.name = 'bothon.png'

        # When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            image_profile=image_profile,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )

        # Then
        self.assertEqual(worker.first_name, first_name)
        # pytest
        assert worker.first_name == first_name
        self.assertEqual(worker.last_name, last_name)
        self.assertEqual(worker.image_profile, image_profile)
        self.assertTrue(worker.is_available)
        # pytest
        assert worker.is_available is True
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)

        os.remove('media/bothon.png')
    
    def test_model_should_have_friendly_name(self):
        first_name = 'Keng'
        last_name = 'Mak'
        is_available = True
        primary_phone = '081-689-777x'
        secondary_phone = '081-689-778x'
        address = 'Geeky Base All Stars'
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )
        assert worker.__str__() == f'{first_name} {last_name}'
