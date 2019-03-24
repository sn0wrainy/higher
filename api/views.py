from django.shortcuts import render
from rest_framework import generics
from api.models import Grade, Candidate
from api.serializers import GradeSerializer, CandidateSerializer


class GradingView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class CandidatesView(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
