# Generated by Django 4.1.7 on 2023-04-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_treatmentplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.BigIntegerField()),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
                ('Document', models.FileField(upload_to='Documents/')),
            ],
            options={
                'db_table': 'Patient_Documents',
            },
        ),
    ]
