from django.shortcuts import render, redirect

from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/crudope/show')
            except:
                pass
    else:
        form = EmployeeForm()
    print("18" + str(form.__doc__))
    print("19" + str(form))
    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/crudope/show")
    return render(request, 'crudope/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/crudope/show")
