# Generated by Django 3.0.7 on 2020-06-28 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_usermodel_next_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='raiting_games_count',
            new_name='rating_games_count',
        ),
    ]
