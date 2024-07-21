from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def frontpage(request):
    return render(request, 'chatapp/frontpage.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'chatapp/signup.html', {'form': form})
def handelogin(request):
    if request.method=="POST":
            # Get the post parameters
        username=request.POST['username']
        password=request.POST['password']
        user_obj=authenticate(request,username= username, password= password)
        if user_obj:
            login(request, user_obj)
            messages.success(request, "Successfully Logged In")
            return redirect("rooms")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("frontpage")
    return render(request,"chatapp/login.html")

def handelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('frontpage')
