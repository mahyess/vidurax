from rest_framework import serializers

from experiments.models import (
    Subject,
    Chapter,
    Experiment,
    ExperimentProcedure,
    QuizQuestion,
    QuizAnswer,
    ChapterObservation,
    AilaTimestamp, StudentCourseStatus,
)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = "__all__"


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True)

    class Meta:
        model = QuizQuestion
        fields = "__all__"


class ExperimentProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentProcedure
        fields = "__all__"


class ChapterObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterObservation
        fields = "__all__"


class ExperimentSerializer(serializers.ModelSerializer):
    procedures = ExperimentProcedureSerializer(many=True)

    class Meta:
        model = Experiment
        fields = "__all__"


class AilaTimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = AilaTimestamp
        fields = "__all__"


class ChapterWithExperimentsSerializer(serializers.ModelSerializer):
    experiments = ExperimentSerializer(many=True)
    quiz_questions = QuizQuestionSerializer(many=True)
    observations = ChapterObservationSerializer(many=True)
    aila_timestamps = AilaTimestampSerializer(many=True)

    class Meta:
        model = Chapter
        fields = "__all__"


class StudentCourseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourseStatus
        fields = "__all__"
