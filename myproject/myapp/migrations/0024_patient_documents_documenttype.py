# Generated by Django 4.1.7 on 2023-04-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_patient_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_documents',
            name='DocumentType',
            field=models.CharField(default='', max_length=50),
        ),
    ]
