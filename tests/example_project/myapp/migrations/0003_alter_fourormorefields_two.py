# Generated by Django 4.2.2 on 2023-06-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_fourorlessfields_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourormorefields',
            name='two',
            field=models.CharField(default='Default', max_length=32, null=True),
        ),
    ]