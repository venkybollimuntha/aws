# Generated by Django 2.0.4 on 2018-05-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180531_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientauthdeatils',
            name='isExisted',
            field=models.BooleanField(default=False),
        ),
    ]