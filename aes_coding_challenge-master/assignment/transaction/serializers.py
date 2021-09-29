from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import BranchMaster,DepartmentMaster,CompanyLedgerMaster,ArticleMaster,ColorMaster
from .models import Transaction,TransactionLineItemDetails,InventoryItem


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields= ["Company","Branch","Department","Transaction_Number","Transaction_Status","Remarks"]



class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLineItemDetails
        fields ="__all__"

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields ="__all__"      
