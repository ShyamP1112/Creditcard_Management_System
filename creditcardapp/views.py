from django.shortcuts import render,redirect
from .form import usersignupForm,creditcardapplyForm,contactsForm
from .models import usersignup,creditcardapply,contacts

# Create your views here.
def index(request):
    user = request.session.get('user')
    if request.method == 'POST':  # root
        if request.POST.get('signup') == 'signup':
            username = ""
            newuser = usersignupForm(request.POST)
            if newuser.is_valid():
                username = newuser.cleaned_data.get('email')
                try:
                    un = usersignup.objects.get(email=username)
                    print("Username is already exists!")
                   
                except usersignup.DoesNotExist:
                    newuser.save()
                    print("User created successfully!")
                   

                return redirect('/')
            else:
                print(newuser.errors)
        elif request.POST.get('login') == 'login':
            unm = request.POST['email']
            pas = request.POST['password']

            user = usersignup.objects.filter(email=unm, password=pas)
            uid = usersignup.objects.get(email=unm)
            print("UserID:", uid.id)
            if user:  # true
                print("Login Successfull!")
                request.session['user'] = unm
                request.session['userid'] = uid.id
                return redirect('home')
            else:
                print("Error! Username or Password does't match.")
    return render(request,'index.html')
    

def home(request):	
    if request.method=='POST':
        mynote=contactsForm(request.POST)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been submitted!")
        else:
            print(mynote.errors)       
    return render(request,'home.html')

def about(request):	     
    return render(request,'about.html')

def creditcard(request):	
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=creditcardapply.objects.get(id=uid)
    if request.method=='POST':
        updateuser=creditcardapplyForm(request.POST)
        if updateuser.is_valid():
            updateuser=creditcardapplyForm(request.POST,instance=cuser)
            updateuser.save()
            print('Your profile has been updated!')
            return redirect('creditcard')
        else:
            print(updateuser.errors)
    return render(request,'creditcard.html',{'user':user,'cuser':creditcardapply.objects.get(id=uid)})     
    

def creditcardform(request):
    if request.method=='POST':
        creditcard=creditcardapplyForm(request.POST,request.FILES)
        if creditcard.is_valid():
            creditcard.save()
            print("Your Account Has been Created!")
        else:
            print(creditcard.errors)	  
            return redirect('creditcard')   
    return render(request,'creditcardform.html')

def services(request):	     
    return render(request,'services.html')

def client(request):	     
    return render(request,'client.html')

def contact(request):	
    if request.method=='POST':
        mynote=contactsForm(request.POST)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been submitted!")
        else:
            print(mynote.errors)     
    return render(request,'contact.html')