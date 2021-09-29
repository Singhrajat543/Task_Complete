# Generated by Django 3.1.1 on 2021-09-28 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_inventoryitem_transaction_transactionlineitemdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='TransactionLineItemDetails',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='transaction.transactionlineitemdetails'),
        ),
        migrations.AddField(
            model_name='transactionlineitemdetails',
            name='Transaction',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction'),
        ),
    ]
