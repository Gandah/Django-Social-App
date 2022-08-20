from django.contrib.auth import logout,login
from django.shortcuts import render, redirect
from .forms import GweetForm
from .models import Gweet, Profile
from .forms import CustomUserCreationForm

# Create your views here.
def dashboard(request):
    return render(request,"users/dashboard.html", {})

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html", {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("gwitter:dashboard")
            


def dashboard_v(request):
    form = GweetForm(request.POST or None)
    if request.method == "POST":
        #form = GweetForm(request.POST)
        if form.is_valid():
            gweet = form.save(commit=False)
            gweet.user = request.user
            gweet.save()
            return redirect("gwitter:dashboard_v")  

    followed_gweets = Gweet.objects.filter(user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at") # arranges gweets in order of latest gweet first

    # form = GweetForm
    return render(request,
     "gwitter/dashboard.html", 
     {"form": form, "gweets": followed_gweets},
     )
    # return render(request,"base.html")

def profile_list(request):
    """
    Render the profile list page.
    @param request - the request object
    @returns the rendered profile list page
    """
    profiles = Profile.objects.exclude(user=request.user)
    return render(request,"gwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    """
        If the user is logged in, then we can follow and unfollow other users.
        @param request - the request to the page.
        @returns the rendered page.
    """
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "gwitter/profile.html", {"profile": profile})

#New functions for user login/register page
def signout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("gwitter:dashboard")
    return render(request, "registration/logout.html", {})


# def password_form(request):
#     return render(request,"registration/password_change_form.html", {})

# def password_form_done(request):
#     return render(request,"registration/password_change_done.html", {})


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username,password)
        
#     return render(request,"registration/login.html", {})


# def logout_view(request):
#     return render(request,"registration/logout.html", {})


# def register_view(request):
#     return render(request,"registration/register.html", {})