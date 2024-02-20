from django.shortcuts import render
import os 
from .forms import*

print(os.getcwd())
# Create your views here.
def employee_list(request):
    return render(request, 'employee/employee_form.html')

def employee_from(request):
    form = EmployeeForm()
    print({'form':form})
    return render(request,'employee/employee_form.html',{'form':form})

    # return HttpResponse('i am working')
    # return render(request, 'employee_form.html')

def employee_deletet(request):
    return render(request, 'employee_form.html')