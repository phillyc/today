# Generated by Django 2.0.13 on 2019-03-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='due',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='parent_task',
            new_name='parent',
        ),
        migrations.RemoveField(
            model_name='task',
            name='actual_time',
        ),
        migrations.RemoveField(
            model_name='task',
            name='estimated_time',
        ),
        migrations.AddField(
            model_name='task',
            name='actual',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='estimated',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]