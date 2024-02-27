from django.shortcuts import render,redirect
from django.http import HttpResponse
from news.models import News
from .forms import UpdateNewsForm

# Create your views here.
def newsdetails(request,newsid):
    news=News.objects.filter(id=newsid).first()
    data={
        'title' : 'New Details for :' + str(newsid),
        'newsid' : newsid,
    }
    if news is not None:
        data['news']=news
    return render(request , 'newsdetails.html' , data)

def newslist(request):
    news=News.objects.all()
    data={
        'title' : "Today's News",
        'news' : news,
    }
    return render(request, 'newslist.html' , data)

def updateNews(request):
    data={
        'title' : "Update News",
    }
    if(request.method=='POST'):
        newsUpdateform=UpdateNewsForm(request.POST)
        if(newsUpdateform.is_valid()):
            newsUpdateform.save()
            return redirect('news-list')
    else:
        # If it's a GET request, create a new instance of the form
        newsUpdateform = UpdateNewsForm()
        data['form']=newsUpdateform
    return render(request, 'updatenews.html' , data)
