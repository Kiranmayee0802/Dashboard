from django.shortcuts import render,redirect
from emp_app.models import Company,Employee
from emp_app.forms import CompanyForm,EmployeeForm, loginForm
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.


def loginCheck(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/emp")
        else:
            messages.info(request, 'invalid credentials')
            return redirect


    else:
        form = loginForm()
        return render(request, "regsitration/login.html")



#Home page
def home(request):
    return redirect(request,"")


# To create Company
def comp(request, id=0):
    if request.method == "GET":
      if id==0:
        form = CompanyForm()

      else:
         form = Company.objects.get(pk=id)  
         form = CompanyForm(instance=form)
      return render(request,"index.html",{'form':form})
    
    else:
       if id==0:
         form = CompanyForm(request.POST)

       else:
           form = Company.objects.get(pk=id) 
           form = CompanyForm(request.POST,instance=form)
    if  form.is_valid():
           form.save()
    return redirect('/show')

# To retrieve Company details
def show(request):
    companies = Company.objects.all()
    return render(request, "show.html", {'companies':companies})

# To Edit Company details
def edit(request, cName):
    company = Company.objects.get(cName=cName)
    return render(request, "edit.html", {'company':company})

# To Update Company
def update(request, cName):
    company = Company.objects.get(cName=cName)
    form = CompanyForm(request.POST, instance= company)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'company': company})

# To Delete Company details
def delete(request, cName):
    company = Company.objects.get(cName=cName)
    company.delete()
    return redirect("/show")


# To create employee

def emp(request, id=0):
    if request.method == "GET":
      if id==0:
        form = EmployeeForm()

      else:
         form = Employee.objects.get(pk=id)  
         form = EmployeeForm(instance=form)
      return render(request,"addemp.html",{'form':form})
    
    else:
       if id==0:
         form = EmployeeForm(request.POST)

       else:
           form = Employee.objects.get(pk=id) 
           form = EmployeeForm(request.POST,instance=form)
    if  form.is_valid():
           form.save()
    return redirect('/showemp')

# def emp(request):
#     if request.method == "POST":

#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
                
#                 form.save()
#                 return redirect("/showemp")
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request, "addemp.html", {'form':form})

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})

# # To update employee details
def updateEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid(): 
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})

# def updateEmp(request, eFname):
#     employee =Employee.objects.get(eFname=eFname)
#     if request.method == "POST":
#         eFname = request.POST['eFname']
#         eLname = request.POST['eLname']
#         eCompany = request.POST['eCompany']
#         eEmail = request.POST['eEmail']
#         ePhone = request.POST['ePhone']
        
#         employee = Employee.objects.filter(eFname=eFname).update(eFname=eFname,eLname=eLname,eCompany=eCompany,eEmail=eEmail,ePhone=ePhone)
#         messages.success(request, "Employee Updated successfully")
#         return redirect('/showemp')
#     return render(request, 'editemployeee.html', {'employee': employee})







