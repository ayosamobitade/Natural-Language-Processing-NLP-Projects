from django.shortcuts import render, redirect
from .review_module import review_model

# Create your views here.

def ReviewPageView(request):
    pred = ''
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            text = request.POST['review_text']
            model = review_model("model", "vectorizer")
            model.clean_data(str(text))
            pred = model.predict()
        else:
            redirect('reviewpage')
    else:
        print('Error Occured')

    return render(request, 'review/review.html',
    {'pred':1
    
    })