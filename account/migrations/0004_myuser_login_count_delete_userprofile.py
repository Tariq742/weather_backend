# Generated by Django 4.2 on 2023-07-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='login_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]