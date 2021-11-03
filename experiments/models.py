from django.db import models
from tinymce.models import HTMLField


class Subject(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="chapters"
    )
    video = models.FileField(
        verbose_name="AILA Video",
        upload_to="images/chapter/videos/",
        null=True,
        blank=True,
    )
    aim = HTMLField(blank=True)
    apparatus = HTMLField(blank=True)
    chemicals_required = HTMLField(blank=True)
    theory = HTMLField(blank=True)
    procedure = HTMLField(blank=True)

    def __str__(self):
        return self.title


class ChapterObservation(models.Model):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name="observations"
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.chapter.title} - {self.title}"


class AilaTimestamp(models.Model):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name="aila_timestamps"
    )
    title = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    step = models.PositiveSmallIntegerField(default=1)
    start_time = models.PositiveSmallIntegerField(default=0)
    stop_time = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.chapter.title} - step {self.condition}"


class Experiment(models.Model):
    title = models.CharField(max_length=255)
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name="experiments"
    )
    icon = models.ImageField(
        upload_to="images/experiment/icons/", null=True, blank=True
    )
    video = models.FileField(
        verbose_name="experiment video",
        upload_to="images/experiment/videos/",
    )

    def __str__(self):
        return self.title


class ExperimentProcedure(models.Model):
    experiment = models.ForeignKey(
        Experiment, on_delete=models.CASCADE, related_name="procedures"
    )
    title = models.CharField(max_length=255)
    icon = models.ImageField(
        upload_to="images/experiment-procedures/icons/", null=True, blank=True
    )
    step = models.PositiveSmallIntegerField(default=1)
    start_time = models.PositiveSmallIntegerField(default=0)
    stop_time = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.experiment.title} - step {self.step}"

    class Meta:
        ordering = ["step"]


class QuizQuestion(models.Model):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name="quiz_questions"
    )
    question = models.CharField(max_length=255)
    icon = models.ImageField(
        upload_to="images/quiz-questions/icons/", null=True, blank=True
    )

    def __str__(self):
        return self.question


class QuizAnswer(models.Model):
    question = models.ForeignKey(
        QuizQuestion, on_delete=models.CASCADE, related_name="answers"
    )
    answer = models.CharField(max_length=255, null=True, blank=True)
    answer_image = models.ImageField(
        upload_to="images/quiz-answers/icons/", null=True, blank=True
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        if self.answer_image:
            return str(self.answer_image)
        return self.answer
