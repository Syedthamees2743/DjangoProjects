from django.shortcuts import redirect, render

from imgapp.models import Image

# Create your views here.

def index(request):
    return render(request, 'imgshow.html')

def add_product(request):
    if request.method == 'POST':
        prodname = request.POST['prodname']
        proddes = request.POST['proddes']
        prodprc_raw = request.POST.get('prodprc', '')
        if prodprc_raw == '':
            prodprc = 0
        else:
            prodprc = int(prodprc_raw)
        image = request.FILES.get('image')

        prd = Image(
            prodname=prodname,
            proddes=proddes,
            prodprc=prodprc,
            image=image,
        )
        print("Save data...")
        prd.save()
        return redirect('show_product')

    return render(request, 'imgshow.html')


def show_product(request):
    prdts = Image.objects.all()
    return render(request, 'show_product.html', {'prdts': prdts})


def edit_product(request, pk):
    prd = Image.objects.get(pk=pk)

    if request.method == 'POST':
        prd.prodname = request.POST['prodname']
        prd.proddes = request.POST['proddes']
        prodprc_raw = request.POST.get('prodprc', '')
        if prodprc_raw != '':
            prd.prodprc = int(prodprc_raw)
        image = request.FILES.get('image')
        if image:
            prd.image = image

        prd.save()
        return redirect('show_product')

    return render(request, 'edit_product.html', {'product': prd})

def delete_product(request,pk):
    prd = Image.objects.get(pk=pk)
    prd.delete()
    return redirect('show_product')