# Generated by Django 4.0.2 on 2022-02-17 14:47

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_post_date_posted_subcomment_comment_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='img/', verbose_name='Image')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='meme',
        ),
        migrations.AddField(
            model_name='post',
            name='meme',
            field=models.ManyToManyField(related_name='posts', to='posts.MemeImage'),
        ),
    ]