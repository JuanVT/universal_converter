# Generated by Django 2.2.2 on 2019-08-11 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'ordering': ['name'],
            },
        ),
    ]
