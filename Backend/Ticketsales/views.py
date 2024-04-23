from django.shortcuts import render #type:ignore
from .models import ConcertModel ,LocationModel  , TimeModel
# Create your views here.


def ConcertListView(request):
    concerts= ConcertModel.objects.all()

    context = {
        "concert":concerts
    }



    return render(request,"Ticketsales/concert.html",context)





def LocationView(request):
    locations= LocationModel.objects.all()

    context = {
        "location":locations,
    }



    return render(request,"Ticketsales/location.html",context)




def Concertdetail(request , concert_id):
    

    concert = ConcertModel.objects.get(pk=concert_id)
    


    context = {
        "Concertdetails" : concert
    }

    return render(request, "Ticketsales/concertdetail.html" , context)











def TimeView(request):

    times = TimeModel.objects.all()

    context = {
        "times" : times,

    }


    return render(request , "Ticketsales/time.html" , context)