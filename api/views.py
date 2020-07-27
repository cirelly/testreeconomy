from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
import requests
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductView(APIView):
    def get(self, request):
        r = requests.get('https://testbankapi.firebaseio.com/products.json')
        r = r.json()
        sumValue1 = sum(product['value'] for product in r.values() if product)
        print(sumValue1)
        return Response({'products': r, 'suma': sumValue1})

    def post(self, request):
        p = requests.post('https://testbankapi.firebaseio.com/products.json',
        json={
            "category": request.data['category'],
            "description": request.data['description'],
            "identification": request.data['identification'],
            "initdate": request.data['initdate'],
            "productname": request.data['productname'],
            "value": request.data['value']
            })
        
        return Response(p.json())

class ProductDetail(APIView):
    def put(self, request):
        p = requests.put('https://testbankapi.firebaseio.com/products/-Lh7-wuYbP7AwpipuxNx.json', json={
            "category": request.data['category'],
            "description": request.data['description'],
            "identification": request.data['identification'],
            "initdate": request.data['initdate'],
            "productname": request.data['productname'],
            "value": request.data['value']
            }
        )
       
        return Response(p.json())


    def delete(self, request):
        r = requests.get('https://testbankapi.firebaseio.com/products/-Lh7-wuYbP7AwpipuxNx.json')
        product = r.json()
        return Response(product)