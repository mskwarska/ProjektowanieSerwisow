# Generated by Django 3.1.3 on 2021-01-09 11:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BiuroKsiegowe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='declaration',
            name='Document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BiuroKsiegowe.document'),
        ),
        migrations.AlterField(
            model_name='declaration',
            name='PIT',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BiuroKsiegowe.pit'),
        ),
        migrations.AlterField(
            model_name='document',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Documents', to='BiuroKsiegowe.client'),
        ),
        migrations.AlterField(
            model_name='document',
            name='CreatedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DocumentCreatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='CreationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 9, 12, 47, 44, 716758)),
        ),
        migrations.AlterField(
            model_name='document',
            name='DocumentType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BiuroKsiegowe.documenttype'),
        ),
        migrations.AlterField(
            model_name='purchasessales',
            name='Currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BiuroKsiegowe.currency'),
        ),
        migrations.AlterField(
            model_name='purchasessales',
            name='Document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BiuroKsiegowe.document'),
        ),
    ]
