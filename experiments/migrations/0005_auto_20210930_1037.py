# Generated by Django 3.2.7 on 2021-09-30 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_alter_experiment_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='experiment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='experiments.experiment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experimentprocedure',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='experiments.experiment'),
        ),
    ]
