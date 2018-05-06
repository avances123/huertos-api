from rest_framework.test import APITestCase
from faker import Factory
from django.contrib.auth import get_user_model
from users.models import Farmer

###### Module configs and inits
fake = Factory.create('es_ES')
######


class UserApiTest(APITestCase):
    """
    """

    def setUp(self):  
        self.user_cls = get_user_model()
        self.user = self.user_cls.objects.create_user(username=fake.user_name(),password=fake.password(),email=fake.email())
        self.client.force_authenticate(user=self.user)



    def test_profile_is_created(self):
        farmer = Farmer.objects.get(user=self.user)
        self.assertIsInstance(farmer,Farmer)

