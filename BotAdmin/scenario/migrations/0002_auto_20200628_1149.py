# Generated by Django 3.0.7 on 2020-06-28 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scenario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='scenario.ScenarioModel', verbose_name='Сценарий'),
        ),
    ]
