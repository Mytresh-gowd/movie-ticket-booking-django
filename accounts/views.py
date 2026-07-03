from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    """May be like to create for the login and registration form"""

    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('accounts')
    context = {
        'form' : form,
    }

    return render(request, 'accounts/register.html', context)
