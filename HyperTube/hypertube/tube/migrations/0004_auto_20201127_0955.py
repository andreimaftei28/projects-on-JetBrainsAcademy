# Generated by Django 2.2 on 2020-11-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0003_auto_20201126_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='video/'),
        ),
    ]