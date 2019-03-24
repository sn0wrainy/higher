from django.shortcuts import render
from rest_framework import generics
from api.models import Grade
from api.serializers import GradeSerializer


class GradingView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class CandidatesView(generics.ListAPIView):
    # to do
    pass
