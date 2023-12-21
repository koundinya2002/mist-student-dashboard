from django.shortcuts import render
from django.http import HttpResponse
from .models import notes
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def upload_files(request):
    if request.method == "POST":
        name = request.POST["name"]
        file2 = request.FILES["file"]
        document = notes.objects.create(file_name=name, file=file2)
        document.save()
        return render(request, 'assigned.html')
    return render(request,'notes.html')

@login_required
def delete_files(request, file):
    if request.method == "POST":
        file3 = notes.objects.get(file_name=file)
        file3.delete()
    return render(request, 'download.html')

@login_required
def download_files(request):
    file = notes.objects.all()
    return render(request, "download.html", {
        "files":file,
    })