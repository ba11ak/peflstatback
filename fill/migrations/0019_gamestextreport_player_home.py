# Generated by Django 2.2.5 on 2019-09-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fill', '0018_gamestextreport_player_trauma'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestextreport_player',
            name='home',
            field=models.IntegerField(default=0, verbose_name='Дома'),
            preserve_default=False,
        ),
    ]