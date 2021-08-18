# Generated by Django 3.1.2 on 2021-08-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lestName', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]