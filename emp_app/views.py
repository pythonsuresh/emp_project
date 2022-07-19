from django.shortcuts import render
from django.http import HttpResponse
from emp_app.models import emp

def read_views(request):
    emp_list=emp.objects.all()
    context={
            'emp_list' : emp_list
            }
    return render(request, 'read.html', context)

def create_views(request):
    if request.method=="POST":
        First_Name= request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Age = request.POST.get('Age')
        Email = request.POST.get('Email')
        Mob= request.POST.get('Mob')
        Adress= request.POST.get('Adress')

        emp_list= emp.objects.create(First_Name=First_Name,  Last_Name=Last_Name, Age=Age,
                                    Email=Email, Mob=Mob,Adress=Adress)
        return HttpResponse("Data saved into database successfully !...")
    else:

        return render(request, 'create.html')

