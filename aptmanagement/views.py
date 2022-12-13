from django.http import HttpResponse
from django.shortcuts import render
from aptmanagement.models import Tenant, Admin, Apartments

# Create your views here.
def IndexViewPage(request) :
    #return HttpResponse ('Welcome to Apartment Management :)')
    #We that these HttpResponses in here, but I think we'll want
    # to be using render instead
    return render(request, 'aptmanagement/index.html')

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

    context = {
        "tenants" : tenants,
        "apartments" : apartments,
        "annual" : annualEarnings,
        "monthly" : monthlyEarnings
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



def DeleteTenant (request,id) :
    data = Tenant.objects.get(id=id)

    data.delete()

    return TenantInfoPage(request)