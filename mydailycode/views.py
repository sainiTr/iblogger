from django.shortcuts import render,redirect,HttpResponse
from home.models import Cources
from Html.models import Digitalpage

def home(request):

    # return HttpResponse("helo ")
    return render(request,'home/home.html')
def cources(request):
    cources = Cources.objects.all()
    cource = {
        'courses':cources,
        'show':True,
        'title':'All Cources'
    }
    return render(request,'home/cources.html',cource)

def courceSearch(request,title):

    cources = Cources.objects.all()
    searchcource = []
    for cource in cources:
        if str(title).lower() in str(cource.title).lower() or str(title).lower() in str(cource.desc).lower() :
            searchcource.append(cource)
    cource = {
        'courses':searchcource,
        'show':len(searchcource)>0,
        'title':title
    }
    return render(request,'home/cources.html',cource)
    # return render(request,'home/cources.html')

def MainCourse(request):
    return HttpResponse(f"Selected Course : ")

def DigitalPage(re):
    if re.method=="POST":
        name = re.POST.get('name')
        page = re.POST.get('page')
        pages = Digitalpage(name= name,page = page)
        pages.save()
        print(name,page)
    return render(re,'home/digitalpage.html')