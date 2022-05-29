# Generated by Django 4.0.4 on 2022-05-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('session', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
