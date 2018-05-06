from rest_framework import serializers
from farms.models import Farm,Zone
from especies.serializers import EspeciesSerializer

class ZoneSerializer(serializers.ModelSerializer):
    especies =  EspeciesSerializer(read_only=True)
    id = serializers.IntegerField(read_only=False,required=False)

    class Meta:
        model = Zone
        fields = '__all__'



class FarmSerializer(serializers.ModelSerializer):
    #zone_set = ZoneSerializer(many=True,read_only=True)
    zone_set = ZoneSerializer(many=True)
    

    class Meta:
        model = Farm
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('zone_set') # Siempre creamos una farm sin zonas
        farm = Farm.objects.create(**validated_data)
        return farm

    def update(self, instance, validated_data):
        orig_ids = set(zone.id for zone in instance.zone_set.all())
        zone_set = validated_data.pop('zone_set')
        for input_zone in zone_set:
            #print(input_zone)
            if 'id' not in input_zone:
                # Si metemos una zona que no tiene id, es nueva
                #print("Creo: %s" % input_zone)
                Zone.objects.create(**input_zone)
            else:
                # Si tiene id, modificamos la existente
                existing_zone =  instance.zone_set.get(id=input_zone['id'])
                for key in input_zone:
                    setattr(existing_zone, key, input_zone[key])
                existing_zone.save()
                #print("Modifico: %s" % input_zone)
                orig_ids.remove(input_zone['id'])

        
        # Borro las que queden
        #print("Borro: %s" % orig_ids)
        instance.zone_set.filter(id__in=orig_ids).delete()


        [setattr(instance, key, validated_data[key]) for key in validated_data]
        instance.save() 
        return instance


