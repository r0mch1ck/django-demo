# Generated by Django 5.1.6 on 2025-03-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер телефона пользователя'),
        ),
    ]
