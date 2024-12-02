from django.db.models import Q
from django.shortcuts import render, HttpResponse

from .models import Employee, Department, Role


def index(request):
    return render(request, 'myfirst.html')


def view_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    print(context)

    return render(request, 'view_emp.html', context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        roles = Role.objects.all().values()
        data = Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, bonus=bonus,
                        role_id

                        =role,
                        phone=phone, hire_date=hire_date)
        data.save()
        return HttpResponse("Employee data added successfully")

    elif request.method == "GET":
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {'departments': departments, 'roles': roles}
        return render(request, 'add_emp.html', context)

    else:
        return HttpResponse("Something went wrong!")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_del = Employee.objects.get(id=emp_id)
            if emp_del: emp_del.delete()
            return HttpResponse("Employee removed")
        except:
            return HttpResponse("Something went wrong!")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        dept, role = None, None
        name = request.POST['name']
        try:
            dept = request.POST['dept']
        except:
            pass
        try:
            role = request.POST['role']
            print(role, "afta")
        except:
            pass

        emps = Employee.objects.all()
        print(request.POST)
        #
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept_id=dept)
        if role:
            emps = emps.filter(role_idc=role)
            print(emps, "saad")
        context = {
            'emps': emps
        }
        return render(request, 'view_emp.html', context)

    if request.method == 'GET':
        data = Employee.objects.all()
        departments = Department.objects.all()
        roles = Role.objects.all()
        # context = {'departments': departments, 'roles': roles}
        context = {
            'departments': departments, 'roles': roles
        }
        return render(request, 'filter_emp.html', context)
