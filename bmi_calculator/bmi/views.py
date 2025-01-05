from django.shortcuts import render
from .forms import BMIForm
def calculate_bmi(request):
    result=None
    category=None
    if request.method=='POST':
        form=BMIForm(request.POST)
        if form.is_valid():
            weight=form.cleaned_data['weight']
            height=form.cleaned_data['height']
            bmi=weight/(height**2)
            if bmi<=18.5:
                category='under weight'
            elif 18.5<=bmi<=24.9:
                category='normal weight'
            elif 25<=bmi<=29.9:
                category='over weight'
            else:
                category='obesity'
            result=round(bmi,2)
    else:
        form=BMIForm()
    return render(request,'bmi_calculator.html',{'form':form,'result':result,'category':category})
                
# Create your views here.
