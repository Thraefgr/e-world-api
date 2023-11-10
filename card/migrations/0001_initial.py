# Generated by Django 4.2.7 on 2023-11-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('detail', models.TextField()),
                ('faction', models.PositiveSmallIntegerField(choices=[(1, '-'), (2, '-'), (3, '-'), (4, '-')])),
                ('rarity', models.PositiveSmallIntegerField(choices=[(1, 'Legendary'), (2, 'Epic'), (3, 'Rare'), (4, 'Common')])),
                ('price', models.IntegerField()),
                ('power', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]