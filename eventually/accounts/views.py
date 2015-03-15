from django.shortcuts import render
from django.shortcuts import redirect
import accounts
import accounts.forms

def profile(request):
    return redirect('dashboard')

def create_account(request):
    if request.POST:
        form = accounts.forms.UserForm(request.POST, request.FILES)
        profileForm = accounts.forms.UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profileForm.is_valid():
            user = form.save(False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            profile = profileForm.save(False)
            profile.user = user
            profile.save()

            return redirect('confirmation')
    else:
        form = accounts.forms.UserForm()
        profileForm = accounts.forms.UserProfileForm()
    return render(request, 'account/signup.html', {
        'form': form,
        'profileForm': profileForm,
        })

def confirmation(request):
    return render(request, 'account/confirmation.html')

def login(request):
    return render(request, 'account/login.html')