# Generated by Django 4.2.2 on 2023-06-15 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_todo_due_date_alter_todo_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
