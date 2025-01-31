from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# ✅ Vue pour l'inscription
def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
        
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Compte créé avec succès! Bienvenue!')
            return redirect('/')  # Rediriger vers la page d'accueil
        else:
            messages.error(request, 'Erreur lors de l\'inscription. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# ✅ Vue pour la connexion
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
        
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username}!')
            
            # Redirect to next page if specified
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('/')  # Redirection après connexion
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

# ✅ Vue pour la déconnexion
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté avec succès.')
    return redirect('/accounts/login/')
