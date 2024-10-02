from importlib.metadata import files
from string import punctuation

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contactus.html')

def analyze(request):
    #get the text in terminal
    djtext = request.POST.get('text', 'default')
    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    # check checkbox is on and if it is on then do the task
    if removepunc =="on":
        punctuations=''',.:;'"'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {
            'purpose': 'Remove Punctuations',
            'analyzed_text': analyzed
        }
        djtext= analyzed
    if fullcaps=="on":
        analyzed=""

        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {
            'purpose': 'change to upper case',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {
            'purpose': 'New line removed',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {
            'purpose': 'Extra Spae remover',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if charactercounter=="on":
        analyzed = 0
        for char in djtext:
            if char!=" ":
                analyzed+=1
        params = {
            'purpose': 'Character counter',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if removepunc!="on" and newlineremover!="on" and fullcaps!="on" and charactercounter!="on" and extraspaceremover!="on":
        return HttpResponse("Please choose any function to apply on the text.....")
    return render(request, "analyze.html", params)



