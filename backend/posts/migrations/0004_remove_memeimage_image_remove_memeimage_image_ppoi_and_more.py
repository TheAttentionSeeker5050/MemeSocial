# Generated by Django 4.0.2 on 2022-02-17 15:21

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_memeimage_remove_post_meme_post_meme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memeimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='memeimage',
            name='image_ppoi',
        ),
        migrations.AddField(
            model_name='memeimage',
            name='meme',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.nameFile),
        ),
        migrations.RemoveField(
            model_name='post',
            name='meme',
        ),
        migrations.AddField(
            model_name='post',
            name='meme',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.nameFile),
        ),
    ]