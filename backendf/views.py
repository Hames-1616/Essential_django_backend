import json
from django.http import JsonResponse
from django.http import HttpResponse
from pymongo import MongoClient
import pymongo
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializer import *

def getlog(request):
    client = pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
    db = client['backend']
    collection = db['fetch']
    Email_password = list(collection.find({
        
    },
    {
        '_id':0,
        'Email':1,
        'password':1,
        'phone':1
    })) 
    return JsonResponse(Email_password,safe=False)


def getpop(request):
    client=pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
    db=client['backend']
    collection=db['popular']
    service=list(collection.find({},{
        '_id':0,
        'service':1,
        'image':1,
        'star':1
    }))
    return JsonResponse(service,safe=False)


def getallservices(request):
    client=pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
    db=client['backend']
    collection=db['allservices']
    service=list(collection.find({},
    {
        '_id':0,
        'service':1,
        'image':1
    }))
    return JsonResponse(service,safe=False)


def people(request):
    client=pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
    db=client['backend']
    collection = db['people']
    service = list(collection.find({},
    {
        '_id':0,
        'name':1,
        'star':1,
        'address':1,
        'Email':1,
        'phone':1,
        'active':1
    }))
    return JsonResponse(service,safe=False)

def getservices(request):
    client=pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
    db=client['backend']
    collection=db['services']
    service=list(collection.find({},
    {
        '_id':0,
        'service':1,
        'image':1
    }))
    return JsonResponse(service,safe=False)
'''
def insert(request):
        data=json.loads(request.body)
        Email = data['Email']
        password = data['password']

        client =  pymongo.MongoClient("mongodb://192.168.29.103:27017")
        db = client['backend']
        collection = db['fetch']
        collection.insert_one({'Email':Email,'password':password})
    '''

class EmailPasswordViewSet(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def insert(self,request):
        serializer = EmailPasswordSerializer(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            password = serializer.validated_data['password']

            client =  pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
            db = client['backend']
            collection = db['fetch']
            collection.insert_one({'Email':Email,'password':password})
            return Response({'status': 'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)

class serviceviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def ins(self,request):
        serializer = service(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            star = serializer.validated_data['star']
            address = serializer.validated_data['address']
            Email = serializer.validated_data['Email']
            phone = serializer.validated_data['phone']
            active = serializer.validated_data['active']

            client = pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
            db=client['backend']
            collection=db['people']
            collection.insert_one({
                'name':name,
                'star':star,
                'address':address,
                'Email':Email,
                'phone':phone,
                'active':active
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)
