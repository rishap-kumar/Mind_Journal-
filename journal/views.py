from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import JournalEntry,User
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    error = request.GET.get('error')
    if error is None:
        error = ""
    return render(request,"journal/home.html",{'error':error})

def save_journal(request):
    title = request.POST['title'].strip()
    thought = request.POST['thought'].strip()
    if title =="" or thought=="":
        return HttpResponseRedirect(reverse('home')+"?error=Empty fields are not allowed")
    
    JournalEntry.objects.create(
    user = request.user,
    title = title,
    thought = thought 
    )
    return HttpResponseRedirect(reverse('home'))

@login_required
def view_journal(request):
    journal = JournalEntry.objects.filter(user = request.user)
    print("Type:",type(journal))
    return render(request,'journal/journal_list.html',{'journal':journal})

def update_journal(request):
    title = request.POST['title']
    thought = request.POST['thought']
    JournalEntry(title=title ,thought= thought).save()
    return HttpResponse("Journal Updated Sucessfully")

def update(request):
    return render(request,'journal/update_journal.html')

def delete_data(request):
    title = 'Corruption' 
    p1 = JournalEntry.objects.filter(title=title)
    p1.delete()
    return HttpResponse("Record deleted")

def login_page(request):
    error = request.GET.get('error')
    if error is None:
        error = ""
    return render(request,'journal/login_page.html',{'error':error})

def signup_page(request):
    error = request.GET.get('error')
    if error == None:
        error = ""
    return render(request,'journal/signup_page.html',{'error': error})

def saveuser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    if User.objects.filter(username=username).exists():
        url = reverse('signup')+"?error=username_exists"
    elif password!=confirm_password:
        url = reverse('signup')+"?error=Password Mismatch"
    else:
        User.objects.create_user(
        username=username,
        password=password)
        url = reverse('login')
    return HttpResponseRedirect(url)

def check_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username = username,password = password)
    if user is not None:
        login(request,user)
        url = reverse('home')
    else:
        url = reverse('login')+"?error=Invalid Username or Password"
        
    return HttpResponseRedirect(url)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



num = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in num:
    sum += i 

print(sum)