from django.db import models
from django.db.models.deletion import CASCADE


# Masters required in transaction models
class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=10)


class DepartmentMaster(models.Model):
    name = models.CharField(max_length=20, unique=True)


class CompanyLedgerMaster(models.Model):
    name = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)


class ArticleMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)


class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)



Transaction_CHOICES =(

    ('PENDING','PENDING'),
    ('COMPLETED','COMPLETED'),
    ('CLOSE','CLOSE'),
)

class Transaction(models.Model):
     Id= models.AutoField(primary_key=True)
     Company=models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
     Branch= models.ForeignKey(BranchMaster,on_delete=models.CASCADE)
     Department= models.ForeignKey(DepartmentMaster, on_delete=CASCADE)
     Transaction_Number = models.IntegerField(unique=True) 
     Transaction_Status = models.CharField(max_length=20, choices=Transaction_CHOICES)
     Remarks = models.CharField(max_length=20, null=True)


unit_CHOICES=(
('KG','KG'),
('METRE','METRE'),

)


class TransactionLineItemDetails(models.Model):
    id = models.AutoField(primary_key=True)
    Transaction= models.ForeignKey(Transaction, default="", on_delete=models.CASCADE)
    Article= models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    Colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    Required_on_date = models.DateTimeField(auto_now_add=True)
    Quantity = models.DecimalField(max_digits=10,decimal_places=3)
    Rate_per_unit =models.IntegerField()
    Unit = models.CharField(max_length=30,  choices=unit_CHOICES)

class InventoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    TransactionLineItemDetails= models.ForeignKey(TransactionLineItemDetails, default="", on_delete=models.CASCADE)
    Article= models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    Colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    Company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
    Gross_Quantity= models.DecimalField(max_digits=10 , decimal_places=3)
    Net_Quantity =models.DecimalField(max_digits=10 , decimal_places=3)
    Unit = models.CharField(max_length=30,  choices=unit_CHOICES)
  

