# Generated by Django 4.2.2 on 2023-06-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_todo_due_date_alter_todo_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
