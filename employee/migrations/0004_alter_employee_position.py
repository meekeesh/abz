# Generated by Django 3.2.5 on 2021-10-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.PositiveSmallIntegerField(choices=[(1, 'level 1'), (2, 'level 2'), (3, 'level 3'), (4, 'level 4'), (5, 'level 5')], default=1),
        ),
    ]
