# Generated by Django 2.2.7 on 2020-01-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='from_email',
            field=models.EmailField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default='NULL'),
        ),
    ]