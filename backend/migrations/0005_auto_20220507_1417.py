# Generated by Django 3.2.13 on 2022-05-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_voter_votefor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='pubkey',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='votingoption',
            name='pubkey',
            field=models.TextField(unique=True),
        ),
    ]
