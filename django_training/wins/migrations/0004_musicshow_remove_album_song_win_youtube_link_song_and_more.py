# Generated by Django 4.1.7 on 2023-09-30 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wins', '0003_artist_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'MusicShow',
                'verbose_name_plural': 'MusicShows',
                'db_table': 'music_show',
            },
        ),
        migrations.RemoveField(
            model_name='album',
            name='song',
        ),
        migrations.AddField(
            model_name='win',
            name='youtube_link',
            field=models.CharField(default='https://www.youtube.com/', max_length=200),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wins.album')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
                'db_table': 'song',
            },
        ),
        migrations.AlterField(
            model_name='win',
            name='music_show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wins.musicshow'),
        ),
        migrations.AlterField(
            model_name='win',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wins.song'),
        ),
    ]