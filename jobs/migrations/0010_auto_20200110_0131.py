# Generated by Django 2.1 on 2020-01-10 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_job_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
