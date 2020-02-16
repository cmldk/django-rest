# Generated by Django 2.2.3 on 2020-02-14 13:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 13, 35, 31, 151490, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2020, 2, 14, 13, 35, 41, 976286, tzinfo=utc), upload_to='media/post/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 13, 35, 47, 613703, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2020, 2, 14, 13, 36, 4, 82828, tzinfo=utc), editable=False, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
