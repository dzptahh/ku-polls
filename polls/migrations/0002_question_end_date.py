# Generated by Django 4.1.1 on 2022-09-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="end_date",
            field=models.DateTimeField(
                default=None, null=True, verbose_name="date end"
            ),
        ),
    ]
