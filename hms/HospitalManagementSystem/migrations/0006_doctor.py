# Generated by Django 4.1.7 on 2023-05-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagementSystem', '0005_delete_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('designation', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('profile_photo', models.ImageField(upload_to='doctor_profiles/')),
            ],
        ),
    ]