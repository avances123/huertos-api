from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Factory
from django.contrib.auth.models import User
from farms.models import Farm,Zone
from farms.serializers import FarmSerializer
from collections import OrderedDict


###### Module configs and inits
fake = Factory.create('es_ES')
######


class FarmApiTest(APITestCase):
    """
    """

    def setUp(self):  
        self.user = User.objects.create_user(username=fake.user_name(),password=fake.password(),email=fake.email())
        self.client.force_authenticate(user=self.user)

        self.farm = Farm.objects.create(owner=self.user,name=fake.md5())
        self.zones = [Zone.objects.create(farm=self.farm,cols=fake.random_int(1,20),rows=fake.random_int(1,20),x=fake.random_int(1,50),y=fake.random_int(1,50)) for i in range(10)]

            
    #####################################################
    # CRUD FARM
    #####################################################    


    def test_get_farm(self):
        url = reverse('farm-detail',kwargs={'pk': self.farm.id})
        response = self.client.get(url, format='json')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #@override_settings()
    def test_post_farm(self):
        url = reverse('farm-list')
        data = {'owner':self.user.id,'name':fake.md5(),'zone_set':[]}
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_farm(self):
        url = reverse('farm-detail',kwargs={'pk': self.farm.id})
        response = self.client.delete(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_put_farm_same_zones(self):
        url = reverse('farm-detail',kwargs={'pk': self.farm.id})
        serializer = FarmSerializer(self.farm)
        data = {'owner':self.user.id,'name':fake.md5(),'zone_set': serializer.data['zone_set']}
        response = self.client.put(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_put_farm_add_zone(self):
        url = reverse('farm-detail',kwargs={'pk': self.farm.id})
        serializer = FarmSerializer(self.farm)
        serializer.data['zone_set'].append(OrderedDict([('especies', None), ('cols', 8), ('rows', 17), ('x', 42), ('y', 5), ('farm', self.farm.id)]))
        data = {'owner':self.user.id,'name':fake.md5(),'zone_set': serializer.data['zone_set']}
        response = self.client.put(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        farm = Farm.objects.get(id=self.farm.id)
        self.assertEqual(farm.zone_set.count() , 10 + 1)


    def test_put_farm_modify_zone(self):
        url = reverse('farm-detail',kwargs={'pk': self.farm.id})
        serializer = FarmSerializer(self.farm)
        zone = serializer.data['zone_set'][0] 
        serializer.data['zone_set'][0] = OrderedDict([('id',zone['id']),('especies', None), ('cols', 2), ('rows', 2), ('x', 2), ('y', 2), ('farm', self.farm.id)])
        data = {'owner':self.user.id,'name':fake.md5(),'zone_set': serializer.data['zone_set']}
        response = self.client.put(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        farm = Farm.objects.get(id=self.farm.id)
        self.assertEqual(farm.zone_set.count() , 10)

    def test_put_farm_delete_zone(self):
        url = reverse('farm-detail',kwargs={'pk': self.farm.id})
        serializer = FarmSerializer(self.farm)
        data= serializer.data['zone_set'][1:]
        data = {'owner':self.user.id,'name':fake.md5(),'zone_set': data}
        response = self.client.put(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        farm = Farm.objects.get(id=self.farm.id)
        self.assertEqual(farm.zone_set.count() , 10 - 1)


    #####################################################
    # FARM ACTIONS
    #####################################################   

    def test_regar_farm(self):
        url = reverse('farm-regar',kwargs={'pk': self.farm.id})
        response = self.client.post(url, {},format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertQuerysetEqual(self.farm.action_object_actions.all(),['regar','created'],transform=lambda x:x.verb)

    def test_filter_my_huertos(self):
        other_user = User.objects.create_user(username=fake.user_name(),password=fake.password(),email=fake.email())
        Farm.objects.create(owner=other_user,name=fake.md5())

        from django.http import QueryDict
        qdict = QueryDict('',mutable=True)
        qdict.update({'owner__username':self.user.username})

        url = reverse('farm-list') + '?' + qdict.urlencode()
        response = self.client.get(url,format='json')
        self.assertEqual(len(response.data),Farm.objects.filter(owner=self.user).count())




    
        

