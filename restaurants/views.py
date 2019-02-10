from django.shortcuts import render

def first_view(request):
    context = {
        "msg": "Hello world!",
    }
    return render(request, 'rest.html', context)
