import json
from django.http import JsonResponse
from django.http import HttpResponse
from pymongo import MongoClient
import pymongo
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializer import EmailPasswordSerializer

def getlog(request):
    client = pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
    db = client['backend']
    collection = db['fetch']
    Email_password = list(collection.find({
        
    },
    {
        '_id':0,
        'Email':1,
        'password':1
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
