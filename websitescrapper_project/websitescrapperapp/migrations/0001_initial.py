# Generated by Django 4.2.4 on 2023-09-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('stringname', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
