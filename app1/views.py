from django.shortcuts import render

# Create your views here.
def Sample1(request):
    return render(request,'Sample1.html')

def Sample2(request):
    return render(request,'Sample2.html')