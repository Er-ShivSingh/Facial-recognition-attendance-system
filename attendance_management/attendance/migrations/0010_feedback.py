# Generated by Django 4.1.6 on 2023-05-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_alter_attendance_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('feedback', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
