# Generated by Django 3.2.12 on 2022-02-25 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
            preserve_default=False,
        ),
    ]
