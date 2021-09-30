from rest_framework import viewsets
from rest_framework.response import Response

from experiments.models import Subject, Chapter, Experiment
from experiments.serializers import SubjectSerializer, ChapterSerializer, ExperimentSerializer, \
    ChapterWithExperimentsSerializer


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
