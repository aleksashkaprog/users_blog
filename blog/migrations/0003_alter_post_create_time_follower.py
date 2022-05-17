# Generated by Django 4.0.4 on 2022-05-16 12:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_post_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 12, 49, 16, 467609)),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]