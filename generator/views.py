from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
def home(request):
    return render(
        request,'generator/home.html', {'name':"Ricardo"}
    )
def generatedPassword(request):
    generated_password=''
    characters=list(
        'abcdefghijkmnopqrstuvwxyz'
    )
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('@#$%^&*(){}[]'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    length=int(request.GET.get('length',10))
    for x in range(length):
        generated_password+=np.random.choice(characters)
    return render(
        request,'generator/password.html',{'password':generated_password}
    )
def about(request):
    return render(
        request,'generator/about.html'
    )