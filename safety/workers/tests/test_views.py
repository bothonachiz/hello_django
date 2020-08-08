from rest_framework.test import APITestCase

from ..models import Worker


class TestWorkerListView(APITestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get("/workers/")
        # dir use for print everything show all property of variable
        # print(dir(response))
        self.assertEqual(response.status_code, 200)

    def test_view_Should_render_list_of_worker_name(self):

        # # use when want to show all assertionError
        # self.maxDiff = None

        # Given
        Worker.objects.create(
            first_name='Narongvit',
            last_name='Promkhana',
            is_available=True,
            primary_phone='087-784-878x',
            secondary_phone='082-524-818x',
            address='Geeky Base All Star',
        )

        Worker.objects.create(
            first_name='Bothon',
            last_name='Narongvit',
            is_available=True,
            primary_phone='084-874-978x',
            secondary_phone='089-925-848x',
            address='Geeky Base All Star',
        )

        # When
        response = self.client.get("/workers/")

        expected = [
            {
                "first_name": "Narongvit",
                "last_name": "Promkhana",
                "is_available": True,
                "primary_phone": "087-784-878x",
                "secondary_phone": "082-524-818x",
                "address": "Geeky Base All Star",
            },
            {
                "first_name": 'Bothon',
                "last_name": "Narongvit",
                "is_available": True,
                "primary_phone": "084-874-978x",
                "secondary_phone": "089-925-848x",
                "address": "Geeky Base All Star",
            }
        ]

        self.assertEqual(response.data, expected)
