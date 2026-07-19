from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Wuthering Waves Tools"
    context = {'title': title}
    return render(request,'Wuwa/home.html', context)

def material_calc(request):
    context={}
    return render(request,'WuWa/materials.html',context)

