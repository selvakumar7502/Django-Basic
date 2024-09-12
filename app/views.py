from django.shortcuts import *
from .models import emp

# Create your views here.
def new(request):
    return HttpResponse(request,"<h1>hii.....<h1>")

def home(request):
    return render(request,"home.html")

def create(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")

        emp.objects.create(name=name,email=email,age=age)

        return HttpResponse(request,"<h1> Compleated </h1>")
        
    return render(request,"create.html")

def view(request):
    data=emp.objects.all()
    return render(request,"view.html",{"key":data})

def update(request,id):
    employee=get_object_or_404(emp,id=id)
    
    if request.method=="POST":
        employee.name=request.POST.get("name")
        employee.email=request.POST.get("email")
        employee.age=request.POST.get("age")
        employee.save()
        return redirect("/view")
    return render(request,"update.html",{"employee":employee})

def delete(request,id):
    employee=get_object_or_404(emp,id=id)

    if request.method=="POST":
        employee.delete()
        return redirect("/view")
    return render(request,"delete.html",{"employee":employee})