# Generated by Django 5.0.7 on 2024-08-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_contacts_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
