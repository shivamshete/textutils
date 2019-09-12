# i have createdthis file -shivam
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
      return render(request, 'index.html')
    #return HttpResponse("home")

def analyze(request):
    #get thetext
    djtext = request.POST.get('text','default')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = ""
         for char in djtext:
              if char not in punctuations:
                  analyzed=analyzed+char

         params = {'purpose':'remove punctuation','analyzed_text': analyzed}
         return render(request , 'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'capitialize', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newline=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (spaceremove == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'space remove', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (charcount == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'charcount', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else :
      return HttpResponse("errorr")
#def capfirst(request):
    #return HttpResponse("capitalize first")

#def newlineremove(request):
    #return HttpResponse("new line remove")

#def spaceremove(request):
    #return HttpResponse("space remove")

#def charcount(request):
    #return HttpResponse("char count")
