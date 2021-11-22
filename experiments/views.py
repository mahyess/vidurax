import datetime

from django.db.models import Func, F, Sum, Value, ExpressionWrapper, fields
from django.db.models.functions import Coalesce
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from experiments.models import Subject, Chapter, Experiment, StudentCourseStatus
from experiments.serializers import SubjectSerializer, ChapterSerializer, ExperimentSerializer, \
    ChapterWithExperimentsSerializer, StudentCourseStatusSerializer


class SubjectModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ChapterModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chapter.objects.all()
    filterset_fields = ['subject_id']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ChapterWithExperimentsSerializer
        return ChapterSerializer


class ExperimentModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    filterset_fields = ['chapter_id']


class StudentCourseStatusModelViewSet(viewsets.ModelViewSet):
    queryset = StudentCourseStatus.objects.all()
    serializer_class = StudentCourseStatusSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def summary(self, request):
        date = self.request.GET.get('date', str(datetime.datetime.now().date()))
        year, month, day = date.split('-')
        qs = StudentCourseStatus.objects.filter(
            start_time__year=year,
            start_time__month=month,
            start_time__day=day,
        )

        physics_duration = qs.filter(course=StudentCourseStatus.PHYSICS).annotate(
            duration=ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField())
        ).aggregate(total_duration=Coalesce(Sum(F('duration')), Value(datetime.timedelta(seconds=0))))["total_duration"]

        chemistry_duration = qs.filter(course=StudentCourseStatus.CHEMISTRY).annotate(
            duration=ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField())
        ).aggregate(total_duration=Coalesce(Sum(F('duration')), Value(datetime.timedelta(seconds=0))))["total_duration"]

        biology_duration = qs.filter(course=StudentCourseStatus.BIOLOGY).annotate(
            duration=ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField())
        ).aggregate(total_duration=Coalesce(Sum(F('duration')), Value(datetime.timedelta(seconds=0))))["total_duration"]

        return Response({
            "physics": physics_duration,
            "chemistry": chemistry_duration,
            "biology": biology_duration,
        })
