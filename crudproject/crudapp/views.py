from django.shortcuts import redirect, render

from crudapp.models import ProductModel

# Create your views here.

def addproductspage (request):
    return render(request,'index.html')

def addproduct (request):
    if request.method== 'POST':
        pn=request.POST.get('pname')
        qt=int(request.POST.get('qty'))
        dc=request.POST.get('des')
        pr=int(request.POST.get('prc'))

        product=ProductModel(
            prodname=pn,
            quantity=qt,
            description=dc,
            price=pr
        )


        product.save()
        return redirect('addproductpage')
    
def viewproduct(request):
    product=ProductModel.objects.all()
    return render(request,'viewproduct.html',{'pro':product})

def editproduct(request,pk):
    editproducts=ProductModel.objects.get(id=pk)
    return render(request,'editpage.html',{'edpro':editproducts})

def editpage(request,pk):
    if request.method =='POST':
        prdn=ProductModel.objects.get(id=pk)
        prdn.prodname=request.POST.get('pname')
        prdn.quantity=int(request.POST.get('qty'))
        prdn.description=request.POST.get('des')
        prdn.price=int(request.POST.get('prc'))
        prdn.save()
        return redirect('viewproduct')
    else:
        return redirect('addproductpage')

def deleteproduct(request,pk):
    delpro=ProductModel.objects.get(id=pk)
    delpro.delete()
    return redirect('viewproduct')