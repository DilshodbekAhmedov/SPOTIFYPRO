# Generated by Django 4.1 on 2022-09-22 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0002_album_artist_song_album"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="album",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="music.album",
            ),
        ),
    ]
