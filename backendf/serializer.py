from rest_framework import serializers

class EmailPasswordSerializer(serializers.Serializer):
    Email = serializers.CharField()
    password = serializers.CharField()
