# Generated by Django 4.1.2 on 2022-10-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kids',
            name='wearer',
        ),
        migrations.RemoveField(
            model_name='men',
            name='wearer',
        ),
        migrations.RemoveField(
            model_name='women',
            name='wearer',
        ),
        migrations.AlterField(
            model_name='categories',
            name='type',
            field=models.CharField(choices=[('dress', 'dress'), ('skirts', 'skirts'), ('trouser', 'trouser'), ('shirts', 'shirts')], max_length=200, null=True),
        ),
    ]