# Generated by Django 3.2.9 on 2021-11-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interior', '0003_alter_company_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='image',
        ),
    ]