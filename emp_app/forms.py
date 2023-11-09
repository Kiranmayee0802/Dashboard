from django import forms
from emp_app.models import Employee, Login
from emp_app.models import Company

# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

#this is for company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        # fields = "__all__"
        fields = ('cName','cEmail','cUrl')

class loginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"


def __init__(self,*args,**kwargs):
     super(EmployeeForm,self).__init__(*args, **kwargs)
     self.fields['eCompany'].empty_label = "Select"
