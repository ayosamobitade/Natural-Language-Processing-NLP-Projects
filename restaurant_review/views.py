from django.shortcuts import render

# Create your views here.

def ReviewPageView(request):
    return render(request, 'review/review.html')