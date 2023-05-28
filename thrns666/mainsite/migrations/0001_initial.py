# Generated by Django 4.2.1 on 2023-05-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=115)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contacts', models.CharField(blank=True, max_length=150)),
                ('photo', models.ImageField(upload_to='photos/%y/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]