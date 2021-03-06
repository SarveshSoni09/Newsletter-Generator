# Generated by Django 3.2.6 on 2021-10-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=50)),
                ('volume', models.CharField(max_length=10)),
                ('department_image', models.ImageField(upload_to='images/')),
                ('editorial_desk', models.TextField()),
            ],
        ),
    ]
