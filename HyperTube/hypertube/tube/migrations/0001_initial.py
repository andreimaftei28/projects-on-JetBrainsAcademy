# Generated by Django 2.2 on 2020-11-25 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VideoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_tag', to='tube.Tag')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_file', to='tube.Video')),
            ],
        ),
    ]