# Generated by Django 3.2.6 on 2021-10-01 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=100)),
                ('achievement', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
