# Generated by Django 5.0 on 2024-09-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='user_id',
            field=models.UUIDField(default=None, editable=False, null=True),
        ),
    ]
