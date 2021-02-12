from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from importJson.models import RetreivedData
from importJson.serializers import RetreivedDataSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def retreived_data_list(request):
    # GET list of retreived data, POST new data, DELETE all data

    if request.method == 'GET':
        retrieved_data = RetreivedData.objects.all()
        
        symbol = request.GET.get('symbol', None)
        if symbol is not None:
            retrieved_data = RetreivedData.filter(symbol__icontains=symbol)
        
        retrieved_data_serializer = RetreivedDataSerializer(retrieved_data, many=True)
        return JsonResponse(retrieved_data_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        retrieved_data = JSONParser().parse(request)
        retrieved_data_serializer = RetreivedDataSerializer(data=tutorial_data)
        if retrieved_data_serializer.is_valid():
            retrieved_data_serializer.save()
            return JsonResponse(retrieved_data_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(retrieved_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = RetreivedData.objects.all().delete()
        return JsonResponse({'message': '{} Data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def retreived_data_detail(request, pk):
    # find data by pk (id)

    try: 
        retreived_data = RetreivedData.objects.get(pk=pk) 
    except RetreivedData.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': 
        retrieved_data_serializer = RetreivedDataSerializer(retreived_data) 
        return JsonResponse(retrieved_data_serializer.data)

    elif request.method == 'PUT': 
        retreived_data = JSONParser().parse(request) 
        retrieved_data_serializer = RetreivedDataSerializer(retreived_data, data=retreived_data) 
        if retrieved_data_serializer.is_valid(): 
            retrieved_data_serializer.save() 
            return JsonResponse(retrieved_data_serializer.data) 
        return JsonResponse(retrieved_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        retreived_data.delete() 
        return JsonResponse({'message': 'Data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
    # GET / PUT / DELETE retreived data
    
        
@api_view(['GET'])
def retreived_data_list_all(request):
    # GET all retreived data
        
    if request.method == 'GET':
        retreived_data = RetreivedData.objects.all() 
        retrieved_data_serializer = RetreivedDataSerializer(retreived_data, many=True)
        return JsonResponse(retrieved_data_serializer.data, safe=False)
