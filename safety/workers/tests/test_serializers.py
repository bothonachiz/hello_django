from django.test import TestCase

from ..models import Worker
from ..serializers import WorkerSerializer


class TestSerializer(TestCase):
    def test_serializers_should_return_correct_serializers_data(self):

        worker = Worker.objects.create(
            first_name='Narongvit',
            last_name='Promkhana',
            is_available=True,
            primary_phone='087-784-878x',
            secondary_phone='082-524-818x',
            address='Geeky Base All Star',
        )

        serializers = WorkerSerializer(worker)

        expected = {
            'first_name': 'Narongvit',
            'last_name': 'Promkhana',
            'is_available': True,
            'primary_phone': '087-784-878x',
            'secondary_phone': '082-524-818x',
            'address': 'Geeky Base All Star',
        }

        assert serializers.data == expected
