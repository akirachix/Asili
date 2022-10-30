# Generated by Django 4.1.2 on 2022-10-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_kids_men_women_remove_categories_wearer'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='wearer',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default='SOME STRING', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='kids',
            name='wearer',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default='SOME STRING', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='men',
            name='wearer',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default='SOME STRING', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='women',
            name='wearer',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default='SOME STRING', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='type',
            field=models.CharField(choices=[('dress', 'dress'), ('skirts', 'skirts'), ('trouser', 'trouser'), ('shirts', 'shirts')], max_length=10, null=True),
        ),
    ]
