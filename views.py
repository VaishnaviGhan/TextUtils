# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    spaceremover=request.GET.get('spaceremover','off')
    charcount=request.GET.get('charcount','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremover =="on"):
        analyzed = ""
        for char in djtext:
            if char!='\n':
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (spaceremover =="on"):
        analyzed =""
        for char in djtext:
            if char!=" ":
                analyzed = analyzed + char
        params = {'purpose':'space remover','analyzed_text':analyzed}
        return render(request,'analyze.html', params)
    elif (charcount =="on"):
        analyzed=len(djtext)

        params = {'purpose':'char counter','analyzed_text':analyzed}
        return render(request,'analyze.html',params)



    else:
        return HttpResponse('Error')