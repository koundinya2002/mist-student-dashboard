from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import items

# Create your views here.
@login_required
def home(request):
    item = items.objects.all()
    return render(request, "lost/lost.html", {
        "item": item,
    })