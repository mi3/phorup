from django.shortcuts import render
from phorup.models import My_Photo

# Create your views here.

def list_view(request):
    pics = My_Photo.objects.all()
    context = {'photos': pics}
    return render(request, 'list.html', context)

