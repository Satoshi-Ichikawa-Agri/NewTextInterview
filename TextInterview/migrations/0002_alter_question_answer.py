# Generated by Django 4.1.5 on 2023-01-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextInterview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(max_length=4000),
        ),
    ]
