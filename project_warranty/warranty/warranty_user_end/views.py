from django.shortcuts import render
from myapp.models import Customer

# Create your views here.

def login_page(request):
    return render(request,'warranty_end_user/login_page.html', {})

def login_check(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
                
    all_customers = Customer.objects.all()

    for customer in all_customers:
        if(customer.usernane = username and customer.check_password(password)):
            return render(request,'warranty_end_user/welcome.html',{})

