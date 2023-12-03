# Generated by Django 4.1.3 on 2022-11-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchoperation',
            name='resource_type',
            field=models.CharField(choices=[('orders', 'orders'), ('shipments', 'shipments'), ('trackers', 'trackers'), ('billing', 'billing')], default='orders', max_length=25),
        ),
        migrations.AlterField(
            model_name='batchoperation',
            name='status',
            field=models.CharField(choices=[('queued', 'queued'), ('running', 'running'), ('failed', 'failed'), ('completed', 'completed'), ('completed_with_errors', 'completed_with_errors')], default='queued', max_length=25),
        ),
        migrations.AlterField(
            model_name='datatemplate',
            name='resource_type',
            field=models.CharField(choices=[('orders', 'orders'), ('shipments', 'shipments'), ('trackers', 'trackers'), ('billing', 'billing')], max_length=25),
        ),
    ]