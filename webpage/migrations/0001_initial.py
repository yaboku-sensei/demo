# Generated by Django 3.1.2 on 2021-08-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('comment', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
                ('com', models.CharField(max_length=20)),
            ],
        ),
    ]
