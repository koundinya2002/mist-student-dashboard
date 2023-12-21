from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import snaps


# Create your views here.
def landing(request):
    return render(request, "gallery/landing.html", {})

def gallery(request):
    snap = snaps.objects.all()
    return render(request, "gallery/snapshots.html", {
        "snaps": snap,
    })