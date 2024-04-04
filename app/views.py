from django.shortcuts import render

# Create your views here.


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SensorData

@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sensor_name = data.get('sensor', '')
        sensor_value = data.get('value', '')

        # Save data to database
        SensorData.objects.create(sensor=sensor_name, value=sensor_value)
        
        return JsonResponse({'message': 'Data received successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)
