from django.contrib import admin
from .models import Subject, Chapter, Experiment, ExperimentProcedure, QuizQuestion, QuizAnswer


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False


@admin.register(ExperimentProcedure)
class ExperimentProcedureAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False


@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False
