from django.shortcuts import render, get_object_or_404
from .models import Openings


def all_openings(request):
    data = Openings.objects.all()
    return render(request, 'openings/openings.html', {'data': data})


def opening(request, openings_id):
    data = get_object_or_404(Openings, pk=openings_id)
    return render(request, 'openings/temporary.html', {'data': data})
