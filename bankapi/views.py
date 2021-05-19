from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from . models import Bank,Branche
from . serializers import BankSerializer,BrancheSerializer
from rest_framework.decorators import api_view


def give_format(request):
    return JsonResponse({'Endpoint': '/api/branches/autocomplete?q=<> please use this format'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def autocomplete(request, *args, **kwargs):
    try:
        q = request.query_params.get('q',None)
        if q==None:
            return JsonResponse({'message': 'invalid argument'}, status=status.HTTP_404_NOT_FOUND)
        limit = request.query_params.get('limit', None)
        if limit == None:
            return JsonResponse({'message': 'invalid argument'}, status=status.HTTP_404_NOT_FOUND)
        offset = request.query_params.get('offset', None)
        if q == None:
            return JsonResponse({'message': 'invalid argument'}, status=status.HTTP_404_NOT_FOUND)
        limit=int(limit)
        offset=int(offset)
        queryset = Branche.objects.filter(branch__icontains=q).order_by('ifsc')[offset:offset+limit]
        serializer = BrancheSerializer(queryset, many=True)
        return Response(serializer.data)
    except Branche.DoesNotExist:
        return JsonResponse({'message': 'no result found'}, status=status.HTTP_404_NOT_FOUND)

    # we can also use conn = psycopg2.connect(database="postgres", user='postgres', password='psqd', host='127.0.0.1', port= '5432')
    # cursor = conn.cursor()
    # for getting the data


@api_view(['GET'])
def bank_list(request):
    querySet=Bank.objects.all()
    serializer=BankSerializer(querySet,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search(request):
    return JsonResponse({'message': 'no result found'}, status=status.HTTP_404_NOT_FOUND)
    
