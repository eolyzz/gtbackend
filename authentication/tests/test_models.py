from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):

    def test_creates_user(self):
        user=User.objects.create_user(
            'manhasnoname', 'manhasnoname@gmail.com', 'Ogheneyole12')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'manhasnoname@gmail.com')
    
    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="",email="manhasnoname@gmail.com", password="'Ogheneyole12")


    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(
                username="",email="manhasnoname@gmail.com", password="'Ogheneyole12")
    



    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,username="manhasnoname",email="", password="'Ogheneyole12")


    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(
                username="manhasnoname",email="", password="'Ogheneyole12")


 
    def test_creates_super_user_with_staff_status(self):        
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(
                username="manhasnoname",email="manhasnoname@gmail.com", password="'Ogheneyole12", is_staff=False)

    def test_creates_super_user_with_super_user_status(self):        
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(username="manhasnoname",email="manhasnoname@gmail.com", password="'Ogheneyole12", is_superuser=False)

