from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    #Serialize a field to test the APIView
    name = serializers.CharField(max_length=10)
    