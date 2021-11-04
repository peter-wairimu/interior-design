# Generated by Django 3.2.9 on 2021-11-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interior', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField(max_length=255)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
