# Generated by Django 2.0.7 on 2018-08-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nyaaan',
            name='nyan',
            field=models.CharField(default='にゃーん', max_length=255),
        ),
        migrations.AlterField(
            model_name='nyaaan',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
