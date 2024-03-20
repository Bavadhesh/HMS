# Generated by Django 4.1.7 on 2023-04-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_delete_treatmentplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatmentplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.BigIntegerField()),
                ('purpose', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'treatmentplan',
            },
        ),
    ]
