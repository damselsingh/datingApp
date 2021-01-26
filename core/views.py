from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, SignUpForm, ProfileForm, EditUserChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'core/homepage.html')
    else:
        return HttpResponseRedirect('/')

class user_login(LoginView):
    form_class = LoginForm
    template_name = 'core/user_login.html'

def feeds(request):
    if request.user.is_authenticated:
        form = Profile.objects.all()
        return render(request, 'core/feeds.html', {'form': form})
    else:
        messages.error(request, 'You can not access! Please Login first.')
        return HttpResponseRedirect('/')
    

class user_logout(LogoutView):
    template_name = 'core/homepage.html'

class user_signup(FormView):
    template_name='core/user_signup.html'
    form_class = SignUpForm
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        rawpassword = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=rawpassword)
        login(self.request, user)
        return HttpResponseRedirect('/feeds/')

def my_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Bio = request.POST['Bio']
            profileimage = request.FILES['profileimage']
            Hobbies = request.POST['Hobbies']
            age = request.POST['age']
            new = Profile(Bio=Bio, profileimage=profileimage, Hobbies=Hobbies, age=age, user=request.user)
            new.save()
            return HttpResponseRedirect('/feeds/')              
        else:
            if Profile.objects.filter(user=request.user).exists():
                form2 = Profile.objects.filter(user=request.user)
            else:
                form2 = ProfileForm()
            return render(request, 'core/my_profile.html', {'form2': form2})
    else:
        return HttpResponseRedirect('/')

def profile_edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Profile.objects.get(pk=id)
            forms = ProfileForm(request.POST, request.FILES, instance=pi)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/feeds/')
        else:
            pi = Profile.objects.get(pk=id)
            forms = ProfileForm(instance=pi)
        return render(request, 'core/profile_edit.html', {'form': forms} )
    else:
        return HttpResponseRedirect('/login/')

def user_profile_settings(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/feeds/')
        else:
            form = EditUserChangeForm(instance=request.user)
        return render(request, 'core/user_settings.html', {'form': form})
    else:
        return HttpResponseRedirect('/homepage/')