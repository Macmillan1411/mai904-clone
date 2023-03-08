# Generated by Django 4.1.7 on 2023-03-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('iname', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=40)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
