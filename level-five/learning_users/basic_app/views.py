from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required #this decorator forces the user_logout view to have logged in
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST": # grab the information off the forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid(): # check that the forms are valid
            
            user = user_form.save() # grab info from base user form and saving it to the database
            user.set_password(user.password) # hashing the password
            user.save()

            profile = profile_form.save(commit=False) # False == do not commit the change just yet
            profile.user = user # one to one mapping defined in views/user_form

            if 'profile_pic' in request.FILES: # checking to see if they are uploading a pic before we save
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()



    return render(request, 'basic_app/registration.html', # for the context dict we need to pass along what we 
                            {'user_form': user_form, # expect to be rendered in registration template
                             'profile_form': profile_form,
                             'registered': registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username') # getting username from login.html - <input type="text" name="username"
        password = request.POST.get('password')

        user = authenticate(username=username,password=password) # let django authenticate using one line of code

        if user: # exists and has authenticated
            if user.is_active: # and is active
                login(request,user)
                return HttpResponseRedirect(reverse('index')) # redirects them back to the homepage

            else: 
                return HttpResponse("ACCOUNT NOT ACTIVE")
        
        else: 
            print('Someone tried to log in and failed')
            print("Username: {} and password {}".format(username, password))
            return HttpResponse('invalid login details supplied!')
    else: 
        return render(request, 'basic_app/login.html', {})
