from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# ✅ Vue pour l'inscription
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après inscription
            return redirect('/')  # Rediriger vers la page d'accueil
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# ✅ Vue pour la connexion
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirection après connexion
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

# ✅ Vue pour la déconnexion
def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
