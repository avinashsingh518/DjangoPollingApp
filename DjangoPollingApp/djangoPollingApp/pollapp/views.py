
from django.shortcuts import render, redirect
from rest_framework.views import APIView                     
from rest_framework.response import Response
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

def signup_view(request):
    if request.method == 'POST':
        obj=Register(mobile=request.POST['txtmobile'], emailid =request.POST['txtemail'], firstname =request.POST["txtfname"], lastname =request.POST["txtlname"], username =request.POST["txtuser"], password =request.POST['txtpass'])
        obj.save()
        return render(request, 'signup.html', {"msg":"Registration Successfully"})
    return render(request, 'signup.html')


def login_view(request):
    if request.method=="POST":

       username = request.POST["txtuser"]

       password = request.POST["txtpass"]

       s = Register.objects.filter(username=username,password=password)

       if(s.count()==1):

            request.session['uid'] = request.POST["txtuser"]
            return redirect("index")

       else:

            return render(request,"login.html",{"key":"invalid userid and password"})   

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
    

"""<-------APIView method for serializer----------->"""

class RegisterAPI(APIView):
    def get(self, request):
        queryset = Register.objects.all()
        serializer = RegisterSerializer(queryset, many=True)
        print(request.user)
        return Response({'status': 200, 'payload':serializer.data})
    
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message':'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload':serializer.data, 'message':'your data is save'})
    
    def patch(self,request):
        try:
            stu_obj=Register.objects.get(id=request.data['id'])
            serializer=RegisterSerializer(stu_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message':'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload':serializer.data, 'message':'your data is save'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message':'you have entered invalid id'})

    def put(self,request):
        try:
            stu_obj=Register.objects.get(id=request.data['id'])
            serializer=RegisterSerializer(stu_obj, data=request.data, partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message':'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload':serializer.data, 'message':'your data is save'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message':'you have entered invalid id'})

    def delete(self,request):
        try:
            id=request.GET.get('id')
            stu_obj=Register.objects.get(id=id)
            stu_obj.delete()
            return Response({'status': 200,  'message':'deleted'})

        except Exception as e:
            print(e)
            return Response({'status': 403, 'message':'you have entered invalid id'})

"""<-------APIView method for serializer----------->"""
