# Generated by Django 3.2.5 on 2021-10-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210901_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[(1, 'level 1'), (2, 'level 2'), (3, 'level 3'), (4, 'level 4'), (5, 'level 5')], default=1, max_length=7),
        ),
    ]
