from django.shortcuts import render
from my_business_card_app import forms
from django.http import HttpResponse, HttpResponseRedirect
from my_business_card_app.forms import UserForm, UserProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'my_business_card_app/index.html')

def other(request):
    return render(request, 'my_business_card_app/other.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("USER NOT ACTIVE")
        else:
            return HttpResponse("USER DOESN'T EXIST")
    else:
        return render(request, 'my_business_card_app/login.html')
    
def registration(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()

                registered = True
                return HttpResponseRedirect("/perso/login/")
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

        return render(request, 'my_business_card_app/registration.html', {'user_form':user_form,
                                                                            'profile_form': profile_form,
                                                                            'registered': registered})