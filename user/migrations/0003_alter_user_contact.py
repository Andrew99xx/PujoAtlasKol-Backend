# Generated by Django 5.0 on 2024-10-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_user_pandal_visits"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="contact",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
