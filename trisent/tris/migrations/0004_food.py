# Generated by Django 4.1.7 on 2023-03-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tris', '0003_contact_created_at_contact_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Region', models.CharField(max_length=100)),
                ('Cuisines', models.CharField(choices=[('s', 'Snacks'), ('m', 'Main Course'), ('b', 'Beverages'), ('d', 'Drinks')], max_length=1)),
                ('Ratings', models.PositiveIntegerField(default=0)),
                ('Type', models.CharField(choices=[('veg', 'Veg'), ('non-veg', 'Nonveg')], max_length=50)),
            ],
        ),
    ]