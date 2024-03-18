from django.shortcuts import render,HttpResponse
import joblib

try:
    model=joblib.load('static/insurance_premimum1')
except:
    print('error')
# print(model)

def index(request):

    return render(request,'index.html')

def prediction(request):

    try:
        if request.method=='POST':
            age=int(request.POST['age'])
            sex=int(request.POST['sex'])
            bmi=int(request.POST['bmi'])
            child=int(request.POST['child'])
            smoker=int(request.POST['smoker'])
            region=int(request.POST['region'])
        
            pred=round(model.predict([[age,sex,bmi,child,smoker,region]])[0])

            print(pred)

            data={
                'pred':pred
            } 

            return render(request,'prediction.html',data)
    except:
        print('getting error')

    return render(request,'prediction.html')

def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')