from rest_framework import status
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from faker import Factory
from django.contrib.auth.models import User
from farms.models import Farm
from actstream.actions import follow, unfollow



###### Module configs and inits
fake = Factory.create('es_ES')
######


class ActionApiTest(APITestCase):
    """
    Action stream tests
    """

    def setUp(self):  
        self.user = User.objects.create_user(username=fake.user_name(),password=fake.password(),email=fake.email())
        self.client.force_authenticate(user=self.user)

    #####################################################
    # ACTIONS
    #####################################################

    def test_farm_is_created(self):
        Farm.objects.create(owner=self.user)
        url = reverse('actions-farm-all')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['verb'],'created')

    def test_farm_is_modified(self):
        farm = Farm.objects.create(owner=self.user)
        farm.name = fake.md5()
        farm.save()
        url = reverse('actions-farm-all')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data[0]['verb'],'modified')

    def test_farm_is_modified_add_zone(self):
        farm = Farm.objects.create(owner=self.user)
        farm.zone_set.create()
        farm.save()
        url = reverse('actions-farm-all')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data[0]['verb'],'modified')

    def test_get_my_follows(self):
        """
        Dame los huertos a los que sigo
        """

        other_user = User.objects.create_user(username=fake.user_name(),password=fake.password(),email=fake.email())
        Farm.objects.create(owner=other_user)
        other_farm = Farm.objects.create(owner=other_user,name=fake.md5())
        follow(self.user,other_farm,actor_only=False)
        url = reverse('farm-following')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['id'],other_farm.id)






