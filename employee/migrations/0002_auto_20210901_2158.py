# Generated by Django 3.2.5 on 2021-09-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employment_date',
            field=models.DateField(),
        ),
    ]
