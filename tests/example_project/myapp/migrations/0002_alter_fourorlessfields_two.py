# Generated by Django 4.2.2 on 2023-06-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourorlessfields',
            name='two',
            field=models.CharField(default='Default', max_length=32, null=True),
        ),
    ]