from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from .serializers import *
from .models import *


def wel(request):
    if request.session.has_key('uid'):
        t=Register.objects.filter(username=request.session['uid'])
        return render(request,'a.html', {"res":t, 'udata':request.session['uid']})
    else:
        return redirect('login')


def delete(request):
    s=Register.objects.get(pk=request.GET['q'])
    s.delete()
    return redirect('signup')

@api_view(["GET", "POST"])
def signup_view(request):
    if request.method == "POST":
        try:
            # If the form is submitted, the data is in request.POST
            data = {
                'mobile': request.POST.get('txtmobile'),
                'emailid': request.POST.get('txtemail'),
                'firstname': request.POST.get('txtfname'),
                'lastname': request.POST.get('txtlname'),
                'username' : request.POST.get('txtuser'),
                'password': request.POST.get('txtpass')
            }

            email_check = Register.objects.filter(emailid=data.get('emailid')).exists()

            if email_check:
                # Render the HTML page with an error message
                return render(request, 'signup.html', {
                    "error": "This email is already registered",
                    "data": data  # Pass the current form data back to the page
                })

            serializer = RegisterSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                # Render the HTML page with a success message
                return render(request, 'signup.html', {
                    "success": "User Registered successfully"
                })
            else:
                # Render the HTML page with validation errors
                return render(request, 'signup.html', {
                    "error": serializer.errors,
                    "data": data  # Pass the current form data back to the page
                })

        except Exception as e:
            # Render the HTML page with a generic error message
            return render(request, 'signup.html', {
                "error": f"Error while doing signup: {str(e)}"
            })

    # If the request method is GET, render the empty signup form
    return render(request, 'signup.html')


@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == "POST":
        try:
            # If the form is submitted, get the data from request.POST
            data = {
                'username' : request.POST.get('txtuser'),
                'password': request.POST.get('txtpass')
            }

            username = request.POST["txtuser"]

            password = request.POST["txtpass"]

            s = Register.objects.filter(username=username, password=password)

            if (s.count() == 1):

                request.session['uid'] = request.POST["txtuser"]
                return redirect("index")

            else:

                return render(request, "login.html", {"key": "invalid userid and password"})

        except Exception as e:
            # Render the HTML page with a generic error message
            return render(request, 'login.html', {
                "error": f"Error during login: {str(e)}"
            })

    # For a GET request, render the login page
    return render(request,"login.html")

def logout(request):
    del request.session['uid']
    return redirect('/login')



def index(request):
    if request.session.has_key('uid'):
        questions = Question.objects.all()
        return render(request,'index.html', {"questions":questions, 'udata':request.session['uid']})
    else:
        return redirect('login')

    
def vote(request,pk):
    if request.session.has_key('uid'):
        question = Question.objects.get(id=pk)
        options = question.choices.all()
        return render(request,'vote.html', {"question":question, 'options': options, 'udata':request.session['uid']})
    else:
        return redirect('login')

def result(request, pk):
    if request.session.has_key('uid'):
        question = Question.objects.get(id=pk)
        options = question.choices.all()
        if request.method == 'POST':
            inputvalue = request.POST['choice']
            selection_option = options.get(id=inputvalue)
            selection_option.vote += 5
            selection_option.save()
        return render(request,'result.html', {"question":question, 'options': options, 'udata':request.session['uid']})
    else:
        return redirect('login')
    

