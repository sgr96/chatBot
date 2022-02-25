# Generated by Django 3.2.11 on 2022-01-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default=None, max_length=100)),
                ('Lastname', models.CharField(default=None, max_length=100)),
                ('Number', models.CharField(default=None, max_length=100)),
                ('Email', models.CharField(default=None, max_length=100)),
                ('Username', models.CharField(default=None, max_length=100)),
                ('Password', models.CharField(default=None, max_length=100)),
            ],
            options={
                'db_table': 'UserDetails',
            },
        ),
    ]
