# Generated by Django 5.1 on 2024-08-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_roll', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_roll', models.BigIntegerField()),
            ],
        ),
    ]
