# Generated by Django 5.0.1 on 2024-03-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_gebruikers_organisatie"),
    ]

    operations = [
        migrations.AddField(
            model_name="onderzoek",
            name="omschrijving",
            field=models.TextField(blank=True, null=True),
        ),
    ]
