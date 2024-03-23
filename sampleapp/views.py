from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Itempage(request):
    return render(request,'itempage.html')
def Additem(request):
    if request.method=='POST':
        Name=request.POST['Name']
        price=request.POST['price']
        qunatity=request.POST['qunatity']
        orderno=request.POST['orderno']
        category=request.POST['category']
        description=request.POST['description']
        img=request.FILES.get('file')
        data =  item(Name =Name ,price=price, qunatity=qunatity ,orderno= orderno,category=category,description=description,image=img )
        data.save()
        return redirect('Itemlist')
def Itemlist(request):
    item_detail =item.objects.all()
    return render(request,'viewitem.html',{'viewitem':item_detail})
def Itemdetails(request,id):
    item_detail =item.objects.get(id=id)
    return render(request,'item.html',{'itemdetails':item_detail})
def editpage(request,pk):
    prdts = item.objects.get(id=pk)
    return render(request,'Edit_item.html',{'prdts':prdts})

def edit_item(request,pk):    
    if request.method=='POST':
        prdcts = item.objects.get(id=pk)
        prdcts.Name=request.POST.get('Name')
        prdcts.price=request.POST.get('price')
        prdcts.qunatity=request.POST.get('qunatity')
        prdcts.orderno=request.POST.get('orderno')
        prdcts.category=request.POST.get('category')
        prdcts.description= request.POST.get('description')
        if len(request.FILES)!=0 :
            prdcts.image=request.FILES.get('file')
        prdcts.save()
        return redirect('Itemlist')
    return render(request, 'Edit_item.html',)
def delete(request,pk):
    p = item.objects.filter(id=pk)
    p.delete()
    return redirect('Itemlist')