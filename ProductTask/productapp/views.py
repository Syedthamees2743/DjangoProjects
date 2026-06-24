from django.shortcuts import render, redirect
from productapp.forms import ProductForm
from productapp.models import Product


def home(request):
    form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def add_product(request):

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('show_product')

    else:
        form = ProductForm()

    return render(request,'add_product.html',{'form':form})


def show_product(request):

    display = Product.objects.all()

    return render(request,'show_product.html',{'display':display})


def edit_product(request,pk):

    prod = Product.objects.get(id=pk)

    detail = ProductForm(instance=prod)

    return render(request,'edit_product.html',{'form':detail,'product':prod})


def update_product(request,pk):

    prod = Product.objects.get(id=pk)

    if request.method=="POST":

        form=ProductForm(request.POST,
        instance=prod)

        if form.is_valid():

            form.save()

            return redirect('show_product')

    return redirect('edit_product',pk=pk)


def delete_product(request,pk):

    prod=Product.objects.get(id=pk)

    prod.delete()

    return redirect('show_product')