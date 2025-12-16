from django.shortcuts import render, redirect
from .forms import EmployeeForm, LoginForm
from .models import Employee
from django.core.paginator import Paginator
from django.contrib.auth.models import User


# -------- HOME (PUBLIC) --------
def home(request):
    return render(request, "home.html")


# -------- LOGIN --------
def login_view(request):
    msg = ""
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']

            user = User.objects.filter(username=uname).first()

            if user and user.check_password(pwd):
                request.session['user'] = uname
                return redirect('list')
            else:
                msg = "Invalid credentials"

    return render(request, "login.html", {"form": form, "msg": msg})


def logout_view(request):
    request.session.flush()
    return redirect('home')


# -------- ADD --------
def add_employee(request):
    if not request.session.get('user'):
        return redirect('login')

    msg = ""
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            Employee.objects.create(
                emp_id=form.cleaned_data['emp_id'],
                name=form.cleaned_data['name'],
                department=form.cleaned_data['department'],
                salary=form.cleaned_data['salary']
            )
            msg = "Employee Added Successfully"
            form = EmployeeForm()

    return render(request, "add.html", {"form": form, "msg": msg})


# -------- LIST + SEARCH + PAGINATION --------
def list_employee(request):
    if not request.session.get('user'):
        return redirect('login')

    data = Employee.objects.all()

    query = request.GET.get("q")
    if query:
        data = data.filter(name__icontains=query)

    paginator = Paginator(data, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, "list.html", {"page_obj": page_obj})


# -------- UPDATE --------
def update_employee(request, emp_id):
    if not request.session.get('user'):
        return redirect('login')

    emp = Employee.objects.get(emp_id=emp_id)

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp.name = form.cleaned_data['name']
            emp.department = form.cleaned_data['department']
            emp.salary = form.cleaned_data['salary']
            emp.save()
            return redirect('list')
    else:
        form = EmployeeForm(initial={
            'emp_id': emp.emp_id,
            'name': emp.name,
            'department': emp.department,
            'salary': emp.salary
        })

    return render(request, "update.html", {"form": form})


# -------- DELETE --------
def delete_employee(request, emp_id):
    if not request.session.get('user'):
        return redirect('login')

    Employee.objects.get(emp_id=emp_id).delete()
    return redirect('list')
