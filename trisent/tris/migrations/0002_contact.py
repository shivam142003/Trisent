# Generated by Django 4.1.3 on 2023-02-08 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tris', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
