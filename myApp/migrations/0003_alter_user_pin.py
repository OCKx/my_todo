# Generated by Django 4.1.7 on 2023-05-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_user_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pin',
            field=models.CharField(max_length=4),
        ),
    ]