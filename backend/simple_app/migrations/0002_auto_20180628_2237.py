# Generated by Django 2.0.6 on 2018-06-28 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='creation_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='text',
        ),
    ]
