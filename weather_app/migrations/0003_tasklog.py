# Generated by Django 4.2.3 on 2023-07-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0002_citysearchhistory_country_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=255)),
                ('scheduled_datetime', models.DateTimeField()),
                ('status', models.CharField(choices=[('initiated', 'Initiated'), ('done', 'Done')], default='initiated', max_length=10)),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('time_of_completion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
