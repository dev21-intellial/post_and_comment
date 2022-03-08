# Generated by Django 3.2.12 on 2022-02-26 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_rename_comment_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user_comment',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='desciption',
            new_name='description',
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
