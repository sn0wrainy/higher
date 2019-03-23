from django.contrib import admin
from api.models import Candidate, Recruiter, Task, Grade


class CandidateAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)


class RecruiterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title",)


class GradeAdmin(admin.ModelAdmin):
    list_display = ("candidate", "recruiter", "task", "value",)


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Recruiter, RecruiterAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Grade, GradeAdmin)
