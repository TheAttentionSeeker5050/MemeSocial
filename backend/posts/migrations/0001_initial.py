# Generated by Django 4.0.2 on 2022-02-15 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('meme', models.ImageField(upload_to='../static/img')),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('posted_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]