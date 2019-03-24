from rest_framework import serializers
from api.models import Grade, Candidate


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ("task", "recruiter", "candidate", "value",)

    def validate(self, data):
        try:
            grade = Grade.objects.get(task=data["task"], candidate=data["candidate"])
        except Grade.DoesNotExist:
            grade = None
        if grade is not None:
            raise serializers.ValidationError("Grade already exists")
        return data


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ("id", "full_name", "avg_grade", "grades",)

    full_name = serializers.SerializerMethodField()
    grades = serializers.SerializerMethodField()
    avg_grade = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj}"

    def get_grades(self, obj):
        return [g.value for g in obj.grades.all()]

    def get_avg_grade(self, obj):
        table = [g.value for g in obj.grades.all()]
        if len(table) == 0:
            return None
        return sum(table)/len(table)
