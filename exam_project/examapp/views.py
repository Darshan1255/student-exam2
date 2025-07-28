# from django.shortcuts import render
# from django.contrib.login import authenticate, login
# from django.contrib.login.decorators import login_required
# from django.contrib import messages

# Create your views here.
# def home(request):
#     return render(request, 'examapp/login.html')

# # def home(request):
#     return render(request, 'examapp/otp.html')

# # def home(request):

#     return render(request, 'examapp/registar.html')

    # Make sure you have created this form

# def register_view(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Registration successful")
#             return redirect('login')  # Replace 'auth' with your actual login URL name
#     return render(request, 'examapp/register.html', {'form': form})

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request,user)
#             return redirect('product_list')
#         else:
#             messages.error(request,'Invalid username or password.')
#             return redirect(login)
#     return render(request,'examapp/login.html')

# def verify_otp(request):
#     # Dummy placeholder view to avoid import error. Replace with real logic.
#     messages.info(request, "OTP verification placeholder.")
#     return redirect('product_list')


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
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .forms import RegisterForm
# import random

# # Store OTPs temporarily (in memory)
# otp_store = {}

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             otp = str(random.randint(100000, 999999))
#             otp_store[username] = otp
#             request.session["otp_user"] = username
#             print(f"OTP for {username}: {otp}")
#             messages.info(request, "OTP sent. Check terminal.")
#             return redirect('auth_page')
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('auth_page')
#     return redirect('auth_page')


# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Registration successful! You can now log in.")
#             return redirect('auth_page')
#     else:
#         form = RegisterForm()
#     return render(request, 'examapp/auth.html', {"form": form, "show": "register-form"})


# def verify_otp(request):
#     username = request.session.get("otp_user")
#     if request.method == "POST":
#         entered_otp = request.POST.get("otp")
#         actual_otp = otp_store.get(username)
#         if entered_otp == actual_otp:
#             user = User.objects.get(username=username)
#             login(request, user)
#             del request.session["otp_user"]
#             messages.success(request, "OTP verified. You are now logged in.")
#             return redirect('auth_page')
#         else:
#             messages.error(request, "Invalid OTP. Please try again.")
#             return redirect('auth_page')
#     return render(request, 'examapp/auth.html', {"show": "otp-form"})


# def auth_page(request):
#     form = RegisterForm()
#     return render(request, "examapp/auth.html", {"form": form, "show": "login-form"})


# def logout_view(request):
#     logout(request)
#     messages.info(request, "You have been logged out.")
#     return redirect('auth_page')

# # examapp/views.py
# from django.shortcuts import render, redirect
# from .utils import send_otp

# def request_otp(request):
#     if request.method == 'POST':
#         phone = request.POST['phone']
#         otp = send_otp(phone)
#         request.session['otp'] = otp
#         return render(request, 'verify_otp.html', {'phone': phone})
#     return render(request, 'request_otp.html')

# def verify_otp(request):
#     if request.method == 'POST':
#         entered_otp = request.POST['otp']
#         if entered_otp == request.session.get('otp'):
#             return render(request, 'success.html')
#         else:
#             return render(request, 'verify_otp.html', {'error': 'Invalid OTP'})
#     return redirect('request_otp')
import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Step 2: Send OTP view
def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = random.randint(100000, 999999)

        request.session['otp'] = str(otp)
        request.session['email'] = email

        subject = 'Your OTP for Login'
        message = f'Your OTP is: {otp}'
        from_email = 'tibelidarshan@gmail.com'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)
        return redirect('verify_otp')

    return render(request, 'send_otp.html')


# ✅ Step 3: Verify OTP view — add it just below or above the send_otp_email function
def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if user_otp == session_otp:
            return HttpResponse("✅ OTP Verified Successfully!")
        else:
            return HttpResponse("❌ Invalid OTP. Please try again.")

    return render(request, 'verify_otp.html')