from django.shortcuts import render

# Create your views here.
def dashboard(request):
    user = request.user
    return render(request, 'static_pages/dashboard.html', {
        'user': user,
        })