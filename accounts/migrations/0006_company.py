# Generated by Django 5.1.6 on 2025-04-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_mentorrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('industry', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
