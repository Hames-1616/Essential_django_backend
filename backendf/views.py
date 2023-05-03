import json
from django.http import JsonResponse
from django.http import HttpResponse
from pymongo import MongoClient
import pymongo
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializer import *

railway = "mongodb://mongo:RcwTjBM9oCZZ0e14PmbV@containers-us-west-145.railway.app:6554"

def getlog(request):
    client = pymongo.MongoClient(railway)
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

def getimg(request):
    client = pymongo.MongoClient(railway)
    db = client['backend']
    collection = db['homeimages']
    images = list(collection.find({

    },
    {
        '1':1,
        '2':1,
        '3':1,
        '4':1,
        '5':1,
        '_id':0
    }))
    return JsonResponse(images,safe=False)







def getpop(request):
    client=pymongo.MongoClient(railway)
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
    client=pymongo.MongoClient(railway)
    db=client['backend']
    collection=db['allservices']
    service=list(collection.find({},
    {
        '_id':0,
        'service':1,
        'image':1
    }))
    return JsonResponse(service,safe=False)


def review(request):
    client=pymongo.MongoClient(railway)
    db=client['backend']
    collection=db['reviews']

    request = list(collection.find({},
    {
        '_id':0,
        'Email':1,
        'description':1,
        'star':1,
        'sent':1
    }))
    return JsonResponse(request,safe=False)

def contact(request):
    client=pymongo.MongoClient(railway)
    db=client['backend']
    collection=db['contactus']

    request = list(collection.find({},{
        '_id':0,
        'Email':1,
        'description':1
    }))
    return JsonResponse(request,safe=False)



def previousreview(request):
    client=pymongo.MongoClient(railway)
    db=client['backend']
    collection=db['previousrating']

    request = list(collection.find({},{
        '_id':0,
        'to':1,
        'name':1,
        'category':1,
        'star':1,
        'from':1
    }))
    return JsonResponse(request,safe=False)


def people(request):
    client=pymongo.MongoClient(railway)
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
        'category':1,
        'people':1
    }))
    return JsonResponse(service,safe=False)    

def getservices(request):
    client=pymongo.MongoClient(railway)
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

            client =  pymongo.MongoClient(railway)
            db = client['backend']
            collection = db['fetch']
            collection.insert_one({'Email':Email,'password':password,'phone':phone})
            return Response({'status': 'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)

class contactviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def contactset(self,request):
        serializer = contactservice(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            description = serializer.validated_data['description']

            client =  pymongo.MongoClient(railway)
            db = client['backend']
            collection = db['contactus']

            collection.insert_one({
                'Email':Email,
                'description':description
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)




class reviewserviceset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def place(self,request):
        serializer = reviewservice(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            description = serializer.validated_data['description']
            star = serializer.validated_data['star']
            sent = serializer.validated_data['sent']
            client = pymongo.MongoClient(railway)
            db=client['backend']
            collection=db['reviews']

            collection.insert_one({
                'Email':Email,
                'description':description,
                'star':star,
                'sent':sent
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)


class updatereviewserviceset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def updateplace(self,request):
        serializer = reviewservice(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            description = serializer.validated_data['description']
            star = serializer.validated_data['star']
            sent = serializer.validated_data['sent']
            client = pymongo.MongoClient(railway)
            db=client['backend']
            collection=db['reviews']

            collection.update_one({
                'Email':Email,
                'description':description,
                'sent':sent
            },{
                '$set':{'star':star,}
            })
            return Response({'status':'success'})
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
            people = serializer.validated_data['people']

            client = pymongo.MongoClient(railway)
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
                'category':category,
                'people':people
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

            client = pymongo.MongoClient(railway)
            db= client['backend']
            collection=db['fetch']

            result = collection.update_one({'Email':Email},{
                '$set':{'password':password}
            })

            if result.modified_count==1:
                return Response({'message':'password updated'})
            else:
                return Response({'message':'Failed to update the password'},status=status.HTTP_204_NO_CONTENT)


class insertpreviousstar(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def insertprevious(self,request):
        serializer = previousstarservice(data=request.data)
        if serializer.is_valid():
            to = serializer.validated_data['to']
            name = serializer.validated_data['name']
            category = serializer.validated_data['category']
            star = serializer.validated_data['star']
            by= serializer.validated_data['by']

            client = pymongo.MongoClient(railway)
            db= client['backend']
            collection=db['previousrating']

            collection.insert_one({
                'to':to,
                'name':name,
                'category':category,
                'star':star,
                'by':by
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)


class updatepreviousstar(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def updateprevious(self,request):
        serializer = previousstarservice(data=request.data)
        if serializer.is_valid():
            to = serializer.validated_data['to']
            name = serializer.validated_data['name']
            category = serializer.validated_data['category']
            star = serializer.validated_data['star']
            by= serializer.validated_data['by']

            client = pymongo.MongoClient(railway)
            db= client['backend']
            collection=db['previousrating']

            result= collection.update_one({
                'to':to,
                'name':name,
                'category':category,
                'by':by
            },
            {
                '$set':{
                   'star':star 
                }
            })
            if result.modified_count==1:
                return Response({'message':'star updated'})
            else:
                return Response({'message':'Failed to update the password'},status=status.HTTP_204_NO_CONTENT)





class updatereviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def updatereview(self,request):
        serializer = updatereviewservice(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            star = serializer.validated_data['star']
            Email = serializer.validated_data['Email']
            category = serializer.validated_data['category']

            client = pymongo.MongoClient(railway)
            db= client['backend']
            collection=db['people']

            result = collection.update_one({
                'name':name,
                'Email':Email,
                'category':category
            },{
                '$set': {'star':star}

            })

            if result.modified_count==1:
                return Response({'message':'star updated'})
            else:
                return Response({},status=status.HTTP_204_NO_CONTENT)





class updatestar(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def updaterate(self,request):
        serializer = updatest(data=request.data)
        if serializer.is_valid():
           
            name = serializer.validated_data['name']
            category = serializer.validated_data['category']
            star = serializer.validated_data['star']
            people = serializer.validated_data['people']

            client = pymongo.MongoClient(railway)
            db= client['backend']
            collection=db['people']

            result = collection.update_one({'name':name,'category':category},{
                '$set':{'star':star,'people':people}
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

            client = pymongo.MongoClient(railway)
            db= client['backend']
            collection=db['people']

            result = collection.delete_one({'Email':Email,'description':description})

            if result.deleted_count:
                return Response({'message':'deleted'})
            else:
                return Response({'message':'error'})
            
