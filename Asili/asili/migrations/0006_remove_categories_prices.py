# Generated by Django 4.1.2 on 2022-10-16 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asili', '0005_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='prices',
        ),
    ]
