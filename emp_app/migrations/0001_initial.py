# Generated by Django 4.0.6 on 2022-07-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=40)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=30)),
                ('Mob', models.BigIntegerField()),
                ('Adress', models.CharField(max_length=50)),
            ],
        ),
    ]
