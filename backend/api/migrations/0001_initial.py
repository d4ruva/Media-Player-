# Generated by Django 3.2.9 on 2021-11-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('songfile', models.FileField(upload_to='')),
                ('aurthor', models.CharField(max_length=30)),
            ],
        ),
    ]
