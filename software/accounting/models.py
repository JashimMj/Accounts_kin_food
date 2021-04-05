from django.db import models

# Create your models here.


class CompanyInfoM(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,blank=True,null=True)
    address=models.TextField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField()
    Fax=models.CharField(max_length=50,null=True,blank=True)
    logo=models.ImageField(upload_to='Company',null=True,blank=True)
    objects=models.Manager()

    def companylogo(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url

class clientInformation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=1500, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    objects = models.Manager()

class producerinformatio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    designation=models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=1500, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    objects = models.Manager()

class entryinfo(models.Model):
    id=models.AutoField(primary_key=True)
    Invoice_no = models.CharField(max_length=255, blank=True, null=True)
    Invoice_date = models.DateField(blank=True, null=True)
    Delivery_Date = models.DateField(blank=True, null=True)
    Collection_date = models.DateField(blank=True, null=True)
    Client_Name = models.ForeignKey(clientInformation,on_delete=models.CASCADE,null=True,blank=True)
    Producer_Name = models.ForeignKey(producerinformatio,on_delete=models.CASCADE,null=True,blank=True)
    Amount=models.IntegerField(blank=True, null=True,default=0)
    Received_Amount=models.IntegerField(blank=True, null=True,default=0)
    Product_return=models.IntegerField(blank=True, null=True,default=0)
    objects = models.Manager()








