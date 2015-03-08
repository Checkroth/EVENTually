from django.shortcuts import render
from django.shortcuts import redirect
import accounts
import accounts.forms

def profile(request):
    return redirect('dashboard')

def create_account(request):
    if request.POST:
        form = accounts.forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('dashboard')
    else:
        form = accounts.forms.UserForm()
    return render(request, 'account/signup.html', {
        'form': form,
        })
