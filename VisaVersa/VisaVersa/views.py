from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'main.html')


def reversed(request):
    user_text=request.GET['usertext']
    reversedtext=user_text[::-1]
    return render(request, 'reversedtext.html', {'usertext':user_text, "reversedtext":reversedtext})