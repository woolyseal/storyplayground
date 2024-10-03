from django.test import TestCase
from rpgs.models import RolePlay


class RolePlayModelTest(TestCase):
    def test_roleplay_model_exists(self):
        roleplay = RolePlay.objects.count()
        self.assertGreaterEqual(roleplay, 0)


class FrontEndViewTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_rpg_list(self):
        response = self.client.get('/rpgs/')
        self.assertEqual(response.status_code, 200)
