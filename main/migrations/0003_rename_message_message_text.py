# Generated by Django 4.1.5 on 2023-01-06 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='text',
        ),
    ]
