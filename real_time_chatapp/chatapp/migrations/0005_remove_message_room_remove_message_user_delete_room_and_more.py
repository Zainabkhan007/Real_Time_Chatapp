# Generated by Django 5.0.6 on 2024-07-03 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
