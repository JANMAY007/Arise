from django.shortcuts import render

def all_exams(request):
    return render(request, 'examination/all_exams.html')
