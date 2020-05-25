from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'blog/homepage.html')
# Create your views here.

def contact(request):
    return render(request,'blog/basic.html', {'values':['Если у вас остались вопросы задавайте мне по телефону, ', '(926)729-23-98','email: oleg.shavernev21993@gmail.com']})