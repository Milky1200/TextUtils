
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def analyze(request):
    djtext=request.POST.get('text','default')

    #Check Checkbox Values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlinereover = request.POST.get('newlinereover','off')
    removesextrapaces = request.POST.get('removesextrapaces','off')

    #Check Which Checkbox is On
    if removepunc == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                 analyzed = analyzed+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlinereover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removesextrapaces=="on"):
        analyzed = ""
        for index ,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removes Extra Spaces', 'analyzed_text': analyzed}
    if(removepunc !="on" and removesextrapaces != "on" and fullcaps != "on" and newlinereover != "on"):
        return HttpResponse("Error")
    else:
        return render(request, 'analyze.html', params)
