
from django.contrib import admin
from django.urls import path, include

#from hotel.views import frontpage
#from hotel.views import roompage
from hotel.views import planpage
from hotel.views import FrontpageView
from hotel.views import RoomView
from hotel.views import RoomupView
from hotel.views import RoomdelView
from hotel.views import RoomeditView
from hotel.views import CalendarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', FrontpageView.as_view(), name='frontpage'),
    # path('frontpage/', frontpage, name='frontpage1'),
    path('room/', RoomView.as_view(), name='roompage'),
    path('roomup/', RoomupView.as_view(), name='roomuppage'),
    path('roomdel/<int:pk>', RoomdelView.as_view(), name='roomdelpage'),
    path('roomedit/<int:pk>', RoomeditView.as_view(), name='roomeditpage'),

    # path('room/', roompage, name='roompage'),
    path('plan/', planpage, name='planpage'),

    path('calendar/', CalendarView.as_view(), name='calendar'),
]

