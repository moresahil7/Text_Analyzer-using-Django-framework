#file is created by me


# from django.http import HttpResponse

#code for video 6
# def index(request):
#     return HttpResponse("<h1>Hey</h1> <a href='https://www.bing.com/'>Bing</a>")
# def contact(request):
#     return HttpResponse("Contact me")





from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text' , 'default')
    removepunc=request.POST.get('removepunc' , 'off')
    capitalize=request.POST.get('capitalize','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if capitalize == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params={'purpose':'Capitalized' , 'analyzed_text':analyzed}
        djtext =analyzed
        # return render(request, 'analyze.html', params)
    if newlineremove == "on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                 analyzed = analyzed+char
        params={'purpose':'New line removed' , 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremove == "on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" " ):
                 analyzed = analyzed+char
        params={'purpose':'Extra Space removed' , 'analyzed_text':analyzed}
        djtext=analyzed
       
    if(removepunc != "on" and capitalize !="on" and newlineremove != "on" and extraspaceremove != "on"):
         return HttpResponse("error")  
       
    return render(request, 'analyze.html', params)
   
            
   
    
   

# def capitalize(request):
#     return HttpResponse("capitalize")

# def spaceremove(request):
#     return HttpResponse("spaceremover")

# def charcount(request):
#     return HttpResponse("character count")

