from django.http import HttpResponse
from django.shortcuts import render 
import operator

def home(request):
    return render(request,'home.html')

def eggs(request):
    return HttpResponse('<h1>eggs are awesome</h1>') 

def wordcount(request):
    
    count=0
    fulltext=request.GET['fulltext']
    full=request.GET['full']
   
    fulltext=fulltext.lower()
    wordlist=fulltext.split()
    full=full.lower()
    
    for j in range(len(wordlist)) :
        if wordlist[j]==full:
            count+=1
        
    return render(request, 'counts.html',{'fulltext': fulltext,'count':len(wordlist),'wordcount':count,'full':full,'counts':count})    

def about(request):
    return render(request,'about.html')