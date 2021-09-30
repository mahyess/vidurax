# Generated by Django 3.2.7 on 2021-09-30 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_experiment_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='experiments.chapter'),
        ),
    ]
