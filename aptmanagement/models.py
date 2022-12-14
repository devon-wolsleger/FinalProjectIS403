from django.db import models

# Create your models here.

class Tenant(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, verbose_name ='Person ID')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    rent_start = models.DateField()
    rent_end = models.DateField()
    apartment = models.ForeignKey('Apartments', null=True, blank=True, on_delete=models.SET_NULL)


    # These were causing problems with the POST information during INTEX, but can be used when displaying data
    def __str__(self):

        return self.first_name  

    class Meta:
        db_table = 'Tenant'


class Admin(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, verbose_name ='Tenant ID')
    admin = models.IntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    person = models.OneToOneField(Tenant, models.CASCADE)

    def __str__(self):
        return (self.admin_id) 

    class Meta:
        db_table = 'Admin'


class Apartments(models.Model):
    house = models.CharField(max_length=50)
    rent = models.IntegerField()

    def __str__(self):
        if self.house == "" :
            self.house = "blank"
        return (self.house)

    class Meta:
        db_table = 'Apartments'

