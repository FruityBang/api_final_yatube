# Generated by Django 2.2.16 on 2022-12-03 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_FollowAdded'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
