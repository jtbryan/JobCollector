from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core import serializers
from django.shortcuts import render

from .models import Job
from .serializers import JobSerializer

@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def create_job(request):
    Job.objects.create(title=request.data.get("title"), description=request.data.get("description"))
    
    return Response(serializers.serialize('json', [Job.objects.filter(title=request.data.get("title")).first()]))