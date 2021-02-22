from django.http import HttpResponse
from django.shortcuts import render
import requests

def main(request):
    return render(request, 'main.html')


def reversed(request):
    user_text=request.GET['usertext']
    reversedtext=user_text[::-1]
    countwords=len(user_text.split())
    return render(request, 'reversedtext.html', {'usertext':user_text, "reversedtext":reversedtext, 'countwords':str(countwords)})

def telegrammes(request):
    bot_token='1543435088:AAFh03jn1DMO8UIrAM5cfSMtiqUlxmWkvOE'
    chatID='-508096769'

    def telegram_bot_sendtext(bot_token, chatID, message):
    	url=f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chatID}&parse_mode=Markdown&text={message}'    
    	response=requests.get(url)
    	return response.json()

    response = telegram_bot_sendtext(bot_token, chatID, "Нужен официант к столику 1")
    print(response)
    return HttpResponse("<h1>was sent</h1>")