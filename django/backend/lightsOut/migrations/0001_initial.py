# Generated by Django 3.1.5 on 2021-03-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Wins', models.IntegerField()),
                ('Loses', models.IntegerField()),
            ],
            options={
                'ordering': ('Name',),
            },
        ),
    ]
