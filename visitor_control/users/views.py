from django.shortcuts import render

# Create your views here.
def page_users(request):
    return render(request, 'users.html')