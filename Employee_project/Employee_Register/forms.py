from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name','emp_code','mobile','position']  
        labels = {
            'full_name':'FullName',
            'emp_code':'EMP_CODE',
        }


    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='SELECT'