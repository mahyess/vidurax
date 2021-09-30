from rest_framework import serializers

from experiments.models import Subject, Chapter, Experiment, ExperimentProcedure, QuizQuestion, QuizAnswer, \
    ExperimentObservation


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


class ExperimentObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentObservation
        fields = "__all__"


class ExperimentSerializer(serializers.ModelSerializer):
    procedures = ExperimentProcedureSerializer(many=True)
    observations = ExperimentObservationSerializer(many=True)

    class Meta:
        model = Experiment
        fields = "__all__"


class ChapterWithExperimentsSerializer(serializers.ModelSerializer):
    experiments = ExperimentSerializer(many=True)
    quiz_questions = QuizQuestionSerializer(many=True)

    class Meta:
        model = Chapter
        fields = "__all__"
