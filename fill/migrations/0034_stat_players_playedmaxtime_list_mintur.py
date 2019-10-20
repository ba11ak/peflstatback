# Generated by Django 2.2.5 on 2019-10-08 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fill', '0033_stat_players_playedmaxtime_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat_Players_PlayedMaxTime_List_MinTur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('team', models.CharField(db_index=True, default='', max_length=200, verbose_name='Команда')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('div', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fill.Divs', verbose_name='Дивизион')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fill.Season', verbose_name='Сезон')),
            ],
        ),
    ]