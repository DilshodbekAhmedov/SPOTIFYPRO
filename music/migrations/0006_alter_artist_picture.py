# Generated by Django 4.1 on 2022-10-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0005_alter_song_listened"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="picture",
            field=models.URLField(null=True),
        ),
    ]