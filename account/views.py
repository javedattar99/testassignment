


from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.

def login_page(request):
    form = AuthenticationForm
    if request.method == 'POST':
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            print("login succdessful")
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'form': form,'error':"Invalid Credentials"})


    return render(request,'accounts/login.html',{'form':form})


def logout_page(request):
    if request.method == 'GET':
      logout(request)
    return redirect('index')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=first_name,email=email,password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        login(request,user)
        print("user created successful",user.username)
        print(first_name,last_name,email)
    return redirect('index')

def indexView(request):
    return render(request,'index.html')


def update_view(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.set_password = request.POST['password']
        user.save()
        print("user updated")
        return redirect('index')
    return render(request,'update.html', {'user': user})

def delete_view(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('index')

def registerUserList(request):
    all_user = User.objects.all()
    return render(request,'alluser.html',{'all_user':all_user})