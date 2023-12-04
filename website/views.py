from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import SignUpForm, AddRecordForm
from .models import Record
from django.http import HttpResponse
# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
            
        else:
            messages.success(request, "There was error in loggin in. Try again ...")
            return redirect('home')
            
    else:
        return render(request, "home.html", {'records': records})




def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})




def customer_record(request,pk):
    if request.user.is_authenticated:
        try:
            customer_record = Record.objects.get(id=pk)
        except Record.DoesNotExist:
            customer_record = None
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You need to login to view that page...")
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        record_to_delete = Record.objects.get(id=pk)
        record_to_delete.delete()
        messages.success(request, "Your record has been deleted.")
        return redirect('home')
    else:
        messages.success(request, "You need to login to delete that...")
        return redirect("home")

@login_required    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Record is added")
            return redirect("home")
    else:
        form = AddRecordForm()
    return render(request, "add_record.html", {"form":form})
    
    
@login_required
def update_record(request, pk):
    current_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Record is updated")
            return redirect("home")
    else:
        form = AddRecordForm(instance=current_record)
    return render(request, "update_record.html", {"form":form})

def healthcheck(request):
    return HttpResponse("This is django app 2")



