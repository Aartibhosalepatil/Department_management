from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from dept_app.models import Department

# Create your views here.
def index(request):
    dept = Department.objects.all()

    context={
        'dept': dept
    }
    return render(request,'index.html',context)

def add_dept(request):
    if request.method=='POST':
        dept_name=request.POST.get('dept_name')
        dept_description=request.POST.get('dept_description')
         
        dept=Department(
                dept_name=dept_name,
                dept_description= dept_description
            )
        dept.save()
    return redirect('home')


def edit_dept(request,id):
    dept = Department.objects.all()

    context={
        'dept': dept
    }
    return render(request,'index.html',context)

# def update(request,id):
#     if request.method=='POST':
#         dept_name=request.POST.get('dept_name')
#         dept_description=request.POST.get('dept_description')

#         dept = Department(
#             id=id,
#             dept_name=dept_name,
#             dept_description= dept_description,

#         )
#         dept.save()
#         return redirect('home')
#     return render(request,'index.html')


def update_department(request, id):
    if request.method == "POST":
        dept = get_object_or_404(Department, id=id)
        dept.dept_name = request.POST.get("dept_name")
        dept.dept_description = request.POST.get("dept_description")
        dept.save()
        return redirect('home')  # Redirect to the department listing page

    return redirect('home')  # Redirect if accessed without POST

def delete_dept(request, id):
    dept = get_object_or_404(Department, id=id)  # Get the object
    dept.delete()  # Delete the object
    return redirect('home')  # Redirect to home after deletion