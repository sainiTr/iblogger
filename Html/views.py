from django.shortcuts import render,HttpResponse
from Html.models import Digitalpage
from json import dumps
# Create your views here.
def index(request,page):
    
    data = Digitalpage.objects.filter(name=page)
    
    allnamess = Digitalpage.objects.all()
    names = []
    for i,name in enumerate(allnamess):
        names.append(name)
    names = dumps(names,default=str)
    print(names)

    datalist  ={ 'pages':data,'names':names}
    return render(request,'html_basic.html',datalist)
def show(re,page):
    return HttpResponse(f"Pages:{page}")

