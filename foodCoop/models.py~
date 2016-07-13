from django.db import models

# all the classes needed for the product definition
class Category1(models.Model):
    category1Code       = models.CharField(max_length=6);
    category1Name       = models.CharField(max_length=100);

    def __str__(self):
        return self.category1Code +
               self.category1Name

class Category2(models.Model):
    category2Code       = models.CharField(max_length=6);
    category2Name       = models.CharField(max_length=100);
    category2Category1  = models.ForeignKey(Category1, on_delete=models.CASCADE)

    def __str__(self):
        return self.category2Code +
               self.category2Name

class Category3(models.Model):
    category3Code       = models.CharField(max_length=6);
    category3Name       = models.CharField(max_length=100);
    category3Category2  = models.ForeignKey(Category2, on_delete=models.CASCADE)

    def __str__(self):
        return self.category3Code +
               self.category3Name

class Product(models.Model):

    #types of products in the catalogue
    #Organic: O ; non-organic: NO ; fairtraid: FT
    #
    ORGANIC                 = 'OR'
    NON_ORGANIC             = 'NO'
    FAIR_TRADE              = 'FT'
    VEGAN                   = 'VE'
    PRODUCT_TYPE_OPTIONS    = (
                              (ORGANIC, 'organic'),
                              (NON_ORGANIC, 'Non Organic'),
                              (FAIR_TRADE, 'Fair Trade'),
                              (VEGAN, 'Vegan'),
                                )
    productId               = models.CharField(max_length=6)
    productRetailerCode     = models.CharField(max_length=6)
    productName             = models.CharField(max_length=1000)
    productBrand            = models.CharField(max_length=1000)
    productSizeUnit         = models.CharField(max_length=100)
    productNumberUnits      = models.CharField(max_length=100)
    productNormalPrice      = models.CharField(max_length=100)
    productCurrentPrice     = models.CharField(max_length=100)
    productVAT              = models.CharField(max_length=100)
    productQuantity         = models.CharField(max_length=100)
    productType             = models.CharField(
                                    max_length = 2,
                                    choices = PRODUCT_TYPE_OPTIONS,
                                    default = NON_ORGANIC)
    productCategory1        = models.ForeignKey(Category1)
    productCategory2        = models.ForeignKey(Category2)
    productCategory3        = models.ForeignKey(Category3)

    def __str__(self):
        return self.productCode         +
               self.productName         +
               self.productBrand        +
               self.productSizeUnit     +
               self.productNumberUnits  +
               self.productNormalPrice  +
               self.productCurrentPrice +
               self.productVAT          +
               self.productQuantity     +
               self.productType         +
               self.productCategory1    +
               self.productCategory2    +
               self.productCategory3    +
               self.productRetailer

class Retailer(models.Model):
    retailerId      = models.CharField(max_length=2)
    retailerName    = models.CharField(max_length=100)
    retailerEmail   = models.EmailField()
    retailerWeb     = models.URLField()
    retailerContact = models.CharField(max_length=100)

    def __str__(self):
        return self.retailerId      +
               self.retailerName    +
               self.retailerEmail   +
               self.retailerWeb     +
               self.retailerContact

class Catalogue(models.Model):
    catalogueId                 = models.CharField(max_length=2)
    catalogueDatePublication    = models.DateTimeField('Date of publication')
    catalogueDateLimit          = models.DateTimeField('Date limit while the catalogue is valid')
    catalogueFile               = models.FileField()

    def __str__(self):
        return self.retailerId      +

class Member(models.Model):
    memberCode              = models.CharField(max_length=4)
    memberName              = models.CharField(max_length=50)
    memberSurname           = models.CharField(max_length=50)
    memberEmailAddress      = models.EmailField()
    memberTelephoneNumber   = models.CharField(max_length=15)
    memberInscriptionDate   = models.DateTimeField('Date Inscription')
    memberPayment           = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return  self.memberCode             +
                self.memberName             +
                self.memberSurname          +
                self.memberEmailAddress     +
                self.memberTelephoneNumber  +
                self.memberInscriptionDate  +
                self.payment

class Order(models.Model):
    orderCode              = models.CharField(max_length=4)
    orderDate              = models.DateTimeField('Date of the order')

    def __str__(self):
        return  self.orderCode +
                self.orderDate

class OrderMember(models.Model):
    orderMemberId          = models.CharField(max_length=4)
    orderCode              = models.ForeignKey(Order, on_delete=models.CASCADE)
    orderMember            = models.ForeignKey(Member, on_delete=models.CASCADE)
    orderProduct           = models.ManyToManyField(Product)

    def __str__(self):
        return  self.orderMemberId +
                self.orderCode     +
                self.orderMember

class Payment(models.Model):
    paymentType         = models.CharField(max_length=50)
    paymentMember       = models.CharField(max_length=50)
    paymentConfirmed    = models.CharField(max_length=1)

    def __str__(self):
        return  self.paymentType +
                self.paymentConfirmed
