from django.shortcuts import render


def surveycomp(request):
    return render(request, 'surveys/surcomp.html')