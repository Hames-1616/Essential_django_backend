from rest_framework import serializers

class EmailPasswordSerializer(serializers.Serializer):
    Email = serializers.CharField()
    password = serializers.CharField()
    phone=serializers.CharField()


class updatepassword(serializers.Serializer):
    Email = serializers.CharField()
    password = serializers.CharField()


class service(serializers.Serializer):
    name = serializers.CharField()
    star = serializers.CharField()
    address = serializers.CharField()
    Email = serializers.CharField()
    phone = serializers.CharField()
    active = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    people = serializers.IntegerField()


class deleteservice(serializers.Serializer):
    Email=serializers.CharField()
    description = serializers.CharField()
