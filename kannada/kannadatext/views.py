from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import KannadaText

def store_kannada(request):
    if request.method == 'POST':
        kannada_text = request.POST.get('kannada_text')
        KannadaText.objects.create(kannada_text=kannada_text)
        return render(request, 'success.html')
    return render(request, 'store_kannada.html')

def display_kannada(request):
    kannada_texts = KannadaText.objects.all()
    return render(request, 'display_kannada.html', {'kannada_texts': kannada_texts})