from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request,'warranty_end_user/login_page.html', {})
