# Generated by Django 3.2.6 on 2021-10-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_panel', '0004_auto_20211005_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
    ]