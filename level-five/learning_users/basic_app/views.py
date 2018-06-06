from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request): # check to see if they are registered

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
