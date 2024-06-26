# Generated by Django 4.2.13 on 2024-06-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='quiz_points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_or_hat',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='signup',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='state_code',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
