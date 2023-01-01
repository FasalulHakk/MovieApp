from django.shortcuts import render, redirect
from .models import Mov
from .forms import movform


# Create your views here.
def main(request):
    obj = Mov.objects.all()
    return render(request, 'index.html', {'mov': obj})


def datail(request, mov_id):
    obj = Mov.objects.get(id=mov_id)
    return render(request, 'detail.html', {'movies': obj})


def add_field(request):
    if request.method == 'POST':
        movie = request.POST.get('name')
        desc = request.POST.get('desc')
        yr = request.POST.get('year')
        img = request.FILES['image']
        mov = Mov(name=movie, desc=desc, year=yr, image=img)
        mov.save()

        return redirect('/')
    return render(request,'a_field.html')


def update(request, id):
    model_mov = Mov.objects.get(id=id)
    form_py = movform(request.POST or None, request.FILES, instance=model_mov)
    if form_py.is_valid():
        form_py.save()
        return redirect('/')
    return render(request, 'edit.html', {'formpy': form_py, 'mov_model': model_mov})


def delete(request, id):
    if request.method == 'POST':
        obj = Mov.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
