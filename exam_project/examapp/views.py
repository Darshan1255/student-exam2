from django.shortcuts import render
from django.contrib.login import authenticate, login
from django.contrib.login.decorators import login_required
from django.contrib import messages

# Create your views here.
# def home(request):
#     return render(request, 'examapp/login.html')

# # def home(request):
#     return render(request, 'examapp/otp.html')

# # def home(request):
#     return render(request, 'examapp/registar.html')

    # Make sure you have created this form

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect('login')  # Replace 'auth' with your actual login URL name
    return render(request, 'examapp/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('product_list')
        else:
            messages.error(request,'Invalid username or password.')
            return redirect(login)
    return render(request,'examapp/login.html')

def verify_otp(request):
    # Dummy placeholder view to avoid import error. Replace with real logic.
    messages.info(request, "OTP verification placeholder.")
    return redirect('product_list')


# def logout_view(request):
#     logout(request)
#     return redirect('login')


# def home(request):
#     categories = Category.objects.all()
#     cart_count = request.session.get('cart_count', 0)
#     wishlist_count = request.session.get('wishlist_count', 0)
#     return render(request, 'examapp/home.html', {
#         'categories': categories,
#         'cart_count': cart_count,
#         'wishlist_count': wishlist_count,
#     })

        # Add logic to log in user or show error here
    