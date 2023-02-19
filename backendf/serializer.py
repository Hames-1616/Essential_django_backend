from rest_framework import serializers

class EmailPasswordSerializer(serializers.Serializer):
    Email = serializers.CharField()
    password = serializers.CharField()
    phone=serializers.CharField()


class updatepassword(serializers.Serializer):
    Email = serializers.CharField()
    password = serializers.CharField()


class updatest(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()
    star = serializers.CharField()
    people = serializers.CharField()


class service(serializers.Serializer):
    name = serializers.CharField()
    star = serializers.CharField()
    address = serializers.CharField()
    Email = serializers.CharField()
    phone = serializers.CharField()
    active = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    people = serializers.CharField()


class reviewservice(serializers.Serializer):
    Email = serializers.CharField()
    description = serializers.CharField()
    star = serializers.CharField()
    sent = serializers.CharField()
    

class updatereviewservice(serializers.Serializer):
    name = serializers.CharField()
    star = serializers.CharField()
    Email =serializers.CharField()
    category = serializers.CharField()



class deleteservice(serializers.Serializer):
    Email=serializers.CharField()
    description = serializers.CharField()


class contactservice(serializers.Serializer):
    Email = serializers.CharField()
    description = serializers.CharField()




class previousstarservice(serializers.Serializer):
    to = serializers.CharField()
    name = serializers.CharField()
    category = serializers.CharField()
    star = serializers.CharField()
    by = serializers.CharField()