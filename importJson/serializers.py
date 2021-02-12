from rest_framework import serializers 
from importJson.models import RetreivedData
 
 
class RetreivedDataSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RetreivedData
        fields = ('id',
                  'symbol',
                  'high',
                  'low',
                  'volume',
                  'quoteVolume',
                  'percentChange',
                  'updatedAt')
