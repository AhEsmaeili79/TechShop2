# Generated by Django 5.1.2 on 2025-02-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoleRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('denied_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
