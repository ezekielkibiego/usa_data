# Generated by Django 4.2.13 on 2024-06-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100)),
                ('state_abbrev', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
            ],
        ),
    ]