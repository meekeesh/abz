# Generated by Django 3.2.8 on 2021-10-31 19:13

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='employee.employee'),
        ),
    ]
