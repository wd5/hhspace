from django.shortcuts import render_to_response

def register(request):
    step = request.POST.get('step', '1')
    if step == 2 and request.POST.get('accept') == 1:
        return render_to_response('register/step3.html')
    elif step == 3:
        return render_to_response('register/step3.html')
    else:
        return render_to_response('register/step1.html')

