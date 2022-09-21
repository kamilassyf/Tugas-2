from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchList


def show_watchlist(request):
    data_film_watchlist = WatchList.objects.all()
    done = WatchList.objects.filter(watched="Done").count()
    notYet = WatchList.objects.filter(watched="Not Yet").count()
    
    if done > notYet:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    
    context = {
        'watchlist' : data_film_watchlist,
        'nama' : "Syifa Cahya Kamila",
        'npm' : "2106653230",
        'message' : message
    }
    return render(request,"watchlist.html",context)

def show_xml (request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json (request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")