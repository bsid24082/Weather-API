# Generated by Django 4.2.2 on 2024-02-26 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Weather_API", "0003_alter_weatherdata_temperature"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weatherdata",
            name="humidity",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="pressure",
            field=models.CharField(max_length=30),
        ),
    ]
