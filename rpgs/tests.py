from django.test import TestCase
from rpgs.models import RolePlay
from django.contrib.auth import get_user_model


class RolePlayModelTest(TestCase):
    def setUp(self):
        # self.user = get_user_model().objects.create(username="normaltest", email="normal@user.com", password="foo", nickname="normaltest")
        self.rpg = RolePlay.objects.create(title='My entry title', description='Lorem Ipsum')

    def test_roleplay_model_exists(self):
        roleplay = RolePlay.objects.count()
        self.assertGreaterEqual(roleplay, 0)

    def test_one_rpg(self):
        response = self.client.get('/rpgs/')
        self.assertContains(response, 'My entry title')

    def test_two_rpgs(self):
        RolePlay.objects.create(title='2-title', description='2-body')
        response = self.client.get('/rpgs/')
        self.assertContains(response, 'My entry title')
        self.assertContains(response, '2-title')

    # Test Detail View
    def test_get_absolute_url(self):
        self.assertIsNotNone(self.rpg.get_absolute_url())

    def test_title_in_rpg(self):
        response = self.client.get(self.rpg.get_absolute_url())
        self.assertContains(response, self.rpg.title)

    def test_body_in_rpg(self):
        response = self.client.get(self.rpg.get_absolute_url())
        self.assertContains(response, self.rpg.description)


class RolePlayFormTest(TestCase):
    def test_rpg_add_form_exists(self):
        response = self.client.get('/rpgs/addRPG')
        self.assertEqual(response.status_code, 200)

    def test_rpg_added(self):
        self.client.post('/rpgs/addRPG', {'title': "Super Important Test", 'description':"This is really important."})
        self.assertEqual(RolePlay.objects.last().title, "Super Important Test")


class FrontEndViewTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_rpg_list(self):
        response = self.client.get('/rpgs/')
        self.assertEqual(response.status_code, 200)


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username="normaltest", email="normal@user.com", password="foo", nickname="normaltest")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", email="", password="foo", nickname="")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username="supertest", email="super@user.com", password="foo", nickname="supertest")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="supertest", email="super@user.com", password="foo", nickname="supertest", is_superuser=False)