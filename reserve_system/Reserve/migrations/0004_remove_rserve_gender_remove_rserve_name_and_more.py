# Generated by Django 5.0 on 2023-12-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserve', '0003_rename_coustomuser_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rserve',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='rserve',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rserve',
            name='need',
        ),
        migrations.AddField(
            model_name='rserve',
            name='date',
            field=models.DateField(default='2023-1-1'),
        ),
    ]