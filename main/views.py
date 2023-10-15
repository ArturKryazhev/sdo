from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse

def sing_up(request):
    form = SingUpForm()
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['e_mail']
            password = form.cleaned_data['password2']
            User.objects.create(username = email, password = password)
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            user = User.objects.get(username = email)
            member.objects.create(user = user, first_name = first_name, second_name = second_name, e_mail = email)
            return HttpResponse("registration success")
        # else:
        #     form = SingUpForm()
    context = {'form':form}
    return render(request, 'main/register.html', context)

# Create your views here.
