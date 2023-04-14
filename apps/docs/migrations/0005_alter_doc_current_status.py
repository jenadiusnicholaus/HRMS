# Generated by Django 4.1.5 on 2023-04-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_alter_doc_address_alter_doc_current_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='current_status',
            field=models.CharField(choices=[('active', 'is working(active)'), ('inactive', 'fired(inactive)')], default='active', max_length=10),
        ),
    ]
