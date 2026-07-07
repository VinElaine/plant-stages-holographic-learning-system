from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def stages(request):
    return render(request, "stages.html")

def viewer(request, stage_id):
    return render(request, "viewer.html", {"stage_id": stage_id})

def hologram(request, stage_id):
    return render(request, "hologram.html", {"stage_id": stage_id})