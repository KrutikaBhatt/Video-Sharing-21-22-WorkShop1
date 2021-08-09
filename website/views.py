from django.shortcuts import render
from django.contrib import messages

from .models import User, Comment, NewVideo
from datetime import date
from django.db.models import Q
from django.views.generic import TemplateView,ListView

class HomePageView(TemplateView):
    template_name = 'home.html'


def homepage(request):

    return render(request,'homepage.html',{})


def video(request,pk):
    video = NewVideo.objects.get(pk=pk)
    return render(request,'videoView.html',{'video':video})



def upload(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        thumbnail =  request.FILES['thumbnail']
        video =  request.FILES['video']
        videoobj= NewVideo(user=request.user,title=title,description=desc, date=date.today(),thumbnail=thumbnail,video=video )
        videoobj.save()
        #print('\n\n\n' + request.user + '\n\n')
    return render(request,'upload.html',{})


class SearchResultsView(ListView):
    model = NewVideo
    template_name = 'search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Video.objects.filter(
            Q(title__icontains=query)
        )
