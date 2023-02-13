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


def getstar(request):
    client=pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
    db=client['backend']
    collection=db['star']

    service=list(collection.find({},{
        'id':0,
        'name':1,
        'Email':1,
        'category':1,
        #'peopleinteract':1,
        #'total':1

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
        'active':1,
        'description':1,
        'category':1
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
            phone = serializer.validated_data['phone']

            client =  pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
            db = client['backend']
            collection = db['fetch']
            collection.insert_one({'Email':Email,'password':password,'phone':phone})
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
            description = serializer.validated_data['description']
            category = serializer.validated_data['category']

            client = pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
            db=client['backend']
            collection=db['people']
            collection.insert_one({
                'name':name,
                'star':star,
                'address':address,
                'Email':Email,
                'phone':phone,
                'active':active,
                'description':description,
                'category':category
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)


class updateviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def update(self,request):
        serializer = updatepassword(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            password = serializer.validated_data['password']

            client = pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
            db= client['backend']
            collection=db['fetch']

            result = collection.update_one({'Email':Email},{
                '$set':{'password':password}
            })

            if result.modified_count==1:
                return Response({'message':'password updated'})
            else:
                return Response({'message':'Failed to update the password'},status=status.HTTP_204_NO_CONTENT)





class deleteviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def delete(self,request):
        serializer = deleteservice(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            description = serializer.validated_data['description']

            client = pymongo.MongoClient("mongodb://mongo:gMY3Fk2HOYV7veSfDFYG@containers-us-west-145.railway.app:6554")
            db= client['backend']
            collection=db['people']

            result = collection.delete_one({'Email':Email,'description':description})

            if result.deleted_count:
                return Response({'message':'deleted'})
            else:
                return Response({'message':'error'})
            