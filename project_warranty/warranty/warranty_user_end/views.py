from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request,'warranty_end_user/login_page.html', {})

def login_check(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Validate the username and password here

        print(request.POST)

        # Redirect the user to the welcome page
        if (username!= None):
            return render(request,'warranty_end_user/welcome.html',{})
        else:
            return render('warranty_end_user/no_user.html')
