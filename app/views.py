from django.shortcuts import render , redirect
from django.http import HttpResponse
########################## import tools for registration and login
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
########################## import form and models
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')## Django's login_required function is 
#   used to secure views in your web applications 
#   by forcing the client to authenticate with a valid logged-in User.
###### home page view
def home(request):

    """
    Main page for the user...
    """

    if request.user.is_authenticated:#### whether loged in or not
        user = request.user #### get user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('sana') #### get user data
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})

###login view
def login(request):
    """
    function for login the user 
    """
    ###if method==GET, it simply sends the page back to itself
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else: ####POST
        form = AuthenticationForm(data=request.POST) ####get form data
        if form.is_valid(): ##whether the data is entered correctly or not
            username = form.cleaned_data.get('username') ##get username
            password = form.cleaned_data.get('password') ##get password
            user = authenticate(username = username , password = password) ##authenticate username and password
            if user is not None: ##if the user is not empty
                loginUser(request , user)
                return redirect('home')
        else: ##If the user is empty
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )

##sign up view
def signup(request):
    """
    Registers the user function 
    """
    if request.method == 'GET':###if method==GET, it simply sends the page back to itself
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else: ### for method==POST
        form = UserCreationForm(request.POST)  ###get form data
        context = {
            "form" : form
        }
        if form.is_valid():##whether the data is entered correctly or not
            user = form.save() ## saves user data if the data matches
            if user is not None:##if the user is not empty
                return redirect('login')
        else:##if the data is entered uncorrectly or not
            return render(request , 'signup.html' , context=context)


## add information for todo
@login_required(login_url='login')## Django's login_required function is 
#   used to secure views in your web applications 
#   by forcing the client to authenticate with a valid logged-in User
def add_todo(request):
    """
    This function add the user data to todo list.
    """
    if request.user.is_authenticated:#### whether loged in or not
        user = request.user#### get user
        form = TODOForm(request.POST) 
        if form.is_valid():##whether the data is entered correctly or not
            todo = form.save(commit=False)##Saving with commit = False gets you a model object,
            # then you can add your extra data and save it.
            todo.user = user 
            todo.save() ## save user 
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})

###delete todoes 
def delete_todo(request , id ): ## id is item id
    """
    This function deletes the user data.
    """
    TODO.objects.get(pk = id).delete() ##pk stands for Primary Key and is just a shortcut, according to django's 
    return redirect('home')
###change todoes
def change_todo(request , id  , jarayon):##jarayon is one of the todo model
    """
    This function changes the user data.
    """
    todo = TODO.objects.get(pk = id)##pk stands for Primary Key and is just a shortcut, according to django's 
    todo.jarayon = jarayon
    todo.save()
    return redirect('home')

### signout function
def signout(request):
    """
    This function log out the user from the program
    """
    logout(request)
    return redirect('login')