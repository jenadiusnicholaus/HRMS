# Generated by Django 4.1.5 on 2023-02-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_employee_snils_number_employee_tin_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='snils_number',
            field=models.CharField(blank=True, max_length=200, verbose_name='СНИЛС'),
        ),
    ]
