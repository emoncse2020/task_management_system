# Generated by Django 5.1.6 on 2025-02-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_taskdetail_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='tasks', to='tasks.employee'),
        ),
    ]
