from django.contrib import admin
from django.db import models
from .models import BranchMaster,DepartmentMaster,CompanyLedgerMaster,ArticleMaster,ColorMaster
from .models import Transaction,TransactionLineItemDetails,InventoryItem
# Register your models here.

@admin.register(BranchMaster)
class ColorMasterAdmin(admin.ModelAdmin):
    list_display=['short_name','contact_person_name','gst_number','address1','pin_code','mobile']


@admin.register(DepartmentMaster)
class DepartmentMasterAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(CompanyLedgerMaster)
class CompanyLedgerMasterAdmin(admin.ModelAdmin):
    list_display=['name','gst_number','supplier_status','address1','pin_code','mobile','remarks']

@admin.register(ArticleMaster)
class ArticleMasterAdmin(admin.ModelAdmin):
    list_display=['name','short_name','blend_pct','twists','remarks']


@admin.register(ColorMaster)
class ColorMasterAdmin(admin.ModelAdmin):
    list_display=['article','name','short_name','remarks']



@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['Id','Company','Branch','Department','Transaction_Number','Transaction_Status','Remarks']

@admin.register(TransactionLineItemDetails)
class TransactionLineItemDetailsAdmin(admin.ModelAdmin):
    list_display=['id','Transaction','Article','Colour','Required_on_date','Quantity','Rate_per_unit','Unit']

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display=['id','TransactionLineItemDetails','Article','Colour','Company','Gross_Quantity','Net_Quantity','Unit']    
