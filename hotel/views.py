from multiprocessing import context
from django.shortcuts import render
from .models import Room
from .models import Yoyaku
from .models import Plan
from .models import Calendar
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class FrontpageView(TemplateView):
    template_name = 'hotel/frontpage.html'

#def frontpage(request):
#    return render(request, "hotel/frontpage.html")

class RoomView(ListView):
    template_name = 'hotel/roompage.html'
    model = Room
    #context_object_name = 'orderby_records'
    #queryset = Room.objects.order_by('-room_num')

class RoomupView(CreateView):
    template_name = 'hotel/roomuppage.html'
    model = Room
    fields = ('room_no', 'room_num', 'room_type', 'room_detail', 'room_date1', 'room_date2')
    success_url = reverse_lazy('roompage')
    #context_object_name = 'orderby_records'
    #queryset = Room.objects.order_by('-room_num')

class RoomdelView(DeleteView):
    template_name = 'hotel/roomdelpage.html'
    model = Room
    success_url = reverse_lazy('roompage')
    #context_object_name = 'orderby_records'
    #queryset = Room.objects.order_by('-room_num')

class RoomeditView(UpdateView):
    template_name = 'hotel/roomeditpage.html'
    model = Room
    fields = ('room_no', 'room_num', 'room_type', 'room_detail', 'room_date1', 'room_date2')
    success_url = reverse_lazy('roompage')
    #context_object_name = 'orderby_records'
    #queryset = Room.objects.order_by('-room_num')

#def roompage(request):
#    rooms = Room.objects.all()
#    return render(request, "hotel/roompage.html",{"rooms": rooms})

def planpage(request):
    plans = Plan.objects.all()
    return render(request, "hotel/planpage.html",{"plans": plans})

class CalendarView(ListView):
    template_name = 'hotel/calendar.html'
    model = Calendar
    paginate_by=3
