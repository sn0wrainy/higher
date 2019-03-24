from rest_framework import serializers
from api.models import Grade


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
