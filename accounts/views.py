from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')


def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            # CREATE THE USER USING THE FORM
            # password = form.cleaned_data['password']
            # user = form.save(commit= False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # CREATE THE USER USING THE create_user METHOD
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = User.CUSTOMER
            user.is_active = True  # decide: auto-activate, or send verification email instead
            user.save()
            messages.success(request, "Your account has been registered successfully")
            return redirect("registerUser")
        else:
            print("Ivalid forms")
            print(form.errors)
    else:

        form = UserForm()
    contex = {
        'form': form
    }
    return render(request, 'accounts/registerUser.html', contex)


