from django.test import TestCase
from rpgs.models import RolePlay


class RolePlayModelTest(TestCase):
    def test_roleplay_model_exists(self):
        roleplay = RolePlay.objects.count()
        self.assertGreaterEqual(roleplay, 0)