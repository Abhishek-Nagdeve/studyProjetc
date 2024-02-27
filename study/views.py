from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import usersForm
from service.models import Service


def home(request):
    servicedata = Service.objects.all()
    data = {
        'title' : 'Home Page',
        'bdata' : 'This is b Data',
        'list' : ['PHP' , 'Java' , 'Django'],
        'student_details' : [
            {'name' : 'PK' , 'phone' : 9421934851},
            {'name' : 'Jaadu' , 'phone' : 9421937595}
        ],
        'numbers' : [10,20,30,40,50],
        'servicedata' : servicedata
    }
    return render(request , 'home.html' , data)

def about(request):
    data = {
        'title' : 'about-us'
    }
    if request.method=='GET':
        data['output'] = request.GET.get('output')
    return render(request , 'about.html', data )

def modelDetail(request,modelID):
    return HttpResponse(modelID)

def userForm(request):
    finalans = 0
    try:
        if request.method == 'POST':
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalans = n1+n2
            url = '/about-us/?output={}'.format(finalans)
            return redirect(url)
    except Exception as e:
        print('Error : ', e )

    data = {
        'title':'User Form',
        'finalans' : finalans
    }
    return render(request , 'userform.html' , data)

def submitform(request):
    finalans = 0
    try:
        if request.method == 'POST':
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalans = n1+n2
            url = '/about-us/?output={}'.format(finalans)
    except Exception as e:
        print('Error : ', e )

    data = {
        'title':'User Form',
        'finalans' : finalans
    }
    return render(request , 'submitform.html' , data)

def usingDjangoForms(request):
    finalans = 0
    form = usersForm()
    try:
        if request.method == 'POST':
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalans = n1+n2
    except Exception as e:
        print('Error : ', e )

    data = {
        'title':'Django Form',
        'finalans' : finalans,
        'form': form
    }
    return render(request , 'usingDjangoForm.html' , data)

def calculator(request):
    finalans=0
    data = {
        'title': 'Calculator'
    }
    try:
        if request.method == 'POST':
            if request.POST['num1']=='' or request.POST['num2'] == '':
                data['error'] = True
                return render(request , 'calculator.html' , data)
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            opr = request.POST['opr']

            if opr == '+':
                finalans=n1+n2
            elif opr == '-':
                finalans=n1-n2
            elif opr == '*':
                finalans=n1*n2
            else:
                finalans=n1/n2

            data['finalans'] = finalans
            data['num1'] = n1
            data['num2'] = n2
            return render(request , 'calculator.html' , data)

    except Exception as e:
        print('Error : ' , e)
    return render(request , 'calculator.html' , data)
