# Generated by Django 2.0.1 on 2018-02-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
