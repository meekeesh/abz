# Generated by Django 3.2.8 on 2021-10-31 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='media'),
        ),
    ]
