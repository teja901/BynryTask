# Generated by Django 5.0.7 on 2025-02-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0002_customercomplaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercomplaint',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
