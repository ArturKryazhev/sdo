# Generated by Django 4.2.6 on 2023-10-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_team_leader_remove_team_members_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='e_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]