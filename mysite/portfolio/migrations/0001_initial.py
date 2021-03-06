# Generated by Django 3.2.9 on 2021-11-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название диплома')),
                ('description', models.TextField(blank=True, verbose_name='Описание(по желанию)')),
                ('file', models.FileField(upload_to='', verbose_name='Фотография или другой документ')),
            ],
        ),
    ]
