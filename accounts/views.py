from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from . models import Profile 
from . forms import SignUpForms ,UserForm , ProfileForm 
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages



def SignUp(requset):
    if requset.method == 'POST':
        form=SignUpForms(requset.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username , password=password )
            login(requset,user)
        return redirect("/")
        
    else:
        form=SignUpForms()
    return render(requset , 'registration/signup.html',{'form':form})




def My_Profile(requset):
    my_profile=Profile.objects.get(user=requset.user)
    return render(requset , 'profile/profile.html',{'my_profile':my_profile})


def Edit_My_Profile(requset):
    profile = Profile.objects.get(user=requset.user)
    if requset.method == 'POST':
        userform=UserForm(requset.POST , instance=requset.user)
        profileform=ProfileForm(requset.POST , instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save(commit=False)
            profileform.user=requset.user
            profileform.save()
            return redirect("/accounts/profile")
        
    else:
        userform=UserForm(instance=requset.user)
        profileform=ProfileForm(instance=profile)
    return render(requset , 'profile/edit_profile.html', {'userform':userform ,'profileform':profileform })



def Change_Password(requset):
    if requset.method == 'POST':
        password_form = PasswordChangeForm(requset.user,requset.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('/accounts/password_change/done')
    else:
        password_form = PasswordChangeForm(requset.user)
        # messages.error(requset, 'Please correct the error below.')
        
    return render(requset ,'registration/password_change.html',{'password_form':password_form})
