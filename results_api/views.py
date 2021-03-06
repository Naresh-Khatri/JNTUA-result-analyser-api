from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from results_api import serializers
from results_api import models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    filterset_fields = ['student__id', 'semester']
    #search_fields = ('=student__id', 'subject__semester',)


class SemesterGPAViewSet(viewsets.ModelViewSet):
    queryset = models.SemesterGPA.objects.order_by('-sgpa')
    serializer_class = serializers.SemesterGPASerializer
    filterset_fields = ['student__id', 'semester']
    #search_fields = ('semester', 'student__name','=student__id')


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer
