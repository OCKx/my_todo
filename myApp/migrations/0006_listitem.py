# Generated by Django 4.1.7 on 2023-06-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_remove_member_email_member_username_alter_member_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]
