# Generated by Django 3.0.7 on 2020-06-27 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('url', models.URLField(blank=True, null=True, verbose_name='url')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thimbnail_img/', verbose_name='Thumbnail')),
                ('author_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Имя автора')),
                ('author_link', models.URLField(blank=True, null=True, verbose_name='Ссылка автора')),
                ('author_icon', models.ImageField(blank=True, null=True, upload_to='author_img/', verbose_name='Картинка автора')),
                ('footer', models.CharField(blank=True, max_length=256, null=True, verbose_name='Футер')),
                ('message_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Embeded Message',
                'verbose_name_plural': 'Embeded Messages',
            },
        ),
        migrations.CreateModel(
            name='EmbedPlannerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_in', models.DateTimeField(verbose_name='Начать в')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('is_done', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('embed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planners', to='embed.EmbedModel')),
            ],
        ),
    ]
