import json
import rest_framework
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import History
from .serializers import HistorySerializer
from django.db.models import Sum
from rest_framework.permissions import IsAdminUser
from common.custom_trottle import AllowMethod


class SumView(APIView):
    """
    API endpoint for sum two numbers in query params.
    """
    throttle_classes =[AllowMethod,]
    def get(self,request):
        num1 = int(request.query_params.get('a',0))
        num2 = int(request.query_params.get('b',0))
        History(a=num1,b=num2).save()
        response = {}
        response["result"] = num1+num2
        response=json.dumps(response)
        return Response(response,status.HTTP_200_OK)


class HistoryView(APIView):
    """
    API endpoint to get history.
    """
    permission_classes = [IsAdminUser,]
    def get(self,request):
        query = History.objects.all()
        ser_query = HistorySerializer(query,many=True)
        return Response(ser_query.data,status.HTTP_200_OK)


class TotalView(APIView):
    """
    API endpoint for total of all a and b.
    """
    permission_classes = [IsAdminUser,]
    def get(self,request):
        query = History.objects.all()
        sum_a = int(query.aggregate(Sum('a'))['a__sum'])
        sum_b = int(query.aggregate(Sum('b'))['b__sum'])
        total = sum_a +sum_b
        response = {}
        response['total'] = total
        response = json.dumps(response)
        return Response(response,status.HTTP_200_OK)
