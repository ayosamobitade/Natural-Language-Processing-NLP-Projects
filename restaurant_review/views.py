from django.shortcuts import render

# Create your views here.

def ReviewPageView(request):
    pred = 0
    return render(request, 'review/review.html',
    {'pred':pred
    
    })