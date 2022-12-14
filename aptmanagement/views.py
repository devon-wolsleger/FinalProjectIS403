from django.http import HttpResponse
from django.shortcuts import render
from aptmanagement.models import Tenant, Admin, Apartments

# Create your views here.
def IndexViewPage(request) :
    tenants = Tenant.objects.all()
    apartments = Apartments.objects.all()
    monthlyEarnings = 0
    for tenant in tenants :
            apartment_id = tenant.apartment_id
            for apartment in apartments :
                if apartment_id == apartment.id :
                    monthlyEarnings = monthlyEarnings + apartment.rent

    context = {
        "monthly" : monthlyEarnings,
    }
    return render(request, 'aptmanagement/index.html',context)

def LoginPage(result) :
    #Not sure which html file to use with this one. 
    #There is a cool login page that we could possibly use. 
    return HttpResponse ('Login Here: ')

def TenantInfoPage(request) :
    
    tenants = Tenant.objects.all()
    apartments = Apartments.objects.all()

    monthlyEarnings = 0
    annualEarnings = 0
    for tenant in tenants :
        apartment_id = tenant.apartment_id
        for apartment in apartments :
            if apartment_id == apartment.id :
                annualEarnings = annualEarnings + apartment.rent * 12
                monthlyEarnings = monthlyEarnings + apartment.rent

    numTenants = len(tenants)
    context = {
        "tenants" : tenants,
        "apartments" : apartments,
        "annual" : annualEarnings,
        "monthly" : monthlyEarnings,
        "numTenants" :numTenants
    }

    return render(request, 'aptmanagement/tenants.html', context)

def AddTenant(request) :
    if request.method == 'POST':

        #Create new Tenant
        tenant = Tenant()
        tenant.first_name = request.POST['first_name']
        tenant.last_name = request.POST['last_name']
        tenant.rent_start = request.POST['rent_start_date']  
        tenant.rent_end = request.POST['rent_end_date']
        tenant.phone = request.POST['phone'] 
        tenant.email = request.POST['email']

        #Use existing Apartments or create new Apartment
        data = Apartments.objects.all()
        inDictionary = False
        for apartments in data :
            if apartments.house != request.POST['house'] :
                continue
            elif apartments.house == request.POST['house'] :
                inDictionary = True
                apartment = Apartments.objects.get(house = request.POST['house'])
                
        #Create new Apartment if not already created
        if inDictionary == False :
            apartment = Apartments()
            apartment.house = request.POST['house']
            apartment.rent = request.POST['rent']
            apartment.save()


        tenant.apartment = apartment
        tenant.save()


    return TenantInfoPage(request)

def EditTenant (request, id) :
    tenant = Tenant.objects.get(id = id)
    apartments = Apartments.objects.all()

    context = {
        "tenant" : tenant,
        "apartments" : apartments,
    }
    return render(request, 'aptmanagement/editTenant.html', context)


def UpdateTenant(request, id):
    if request.method == 'POST':
        tenant = Tenant.objects.get(id = id)
        tenant.first_name = request.POST['first_name']
        tenant.last_name = request.POST['last_name']
        tenant.rent_start = request.POST['rent_start_date']  
        tenant.rent_end = request.POST['rent_end_date']
        tenant.phone = request.POST['phone'] 
        tenant.email = request.POST['email']
        
        data = Apartments.objects.all()
        inDictionary = False
        for apartments in data :
            if apartments.house != request.POST['house'] :
                continue
            elif apartments.house == request.POST['house'] :
                inDictionary = True
                apartment = Apartments.objects.get(house = request.POST['house'])
                if apartment.rent != request.POST['rent'] :
                    apartment.rent = request.POST['rent']
                else:
                    continue

        #Create new Apartment if not already created
        if inDictionary == False :
            apartment = Apartments()
            apartment.house = request.POST['house']
            apartment.rent = request.POST['rent']
            apartment.save()


        tenant.apartment = apartment
        
        
        tenant.save()

    return TenantInfoPage(request)



def DeleteTenant (request,id) :
    data = Tenant.objects.get(id=id)

    data.delete()

    return TenantInfoPage(request)