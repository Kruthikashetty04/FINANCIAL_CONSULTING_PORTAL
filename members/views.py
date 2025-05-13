from django.shortcuts import render

# Create your views here.
def publicpage(request):
    return render(request,'Public/base/design.html')

