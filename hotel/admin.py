from django.contrib import admin
from .models import Yoyaku
from .models import Room
from .models import Plan
from .models import Calendar
from .models import Sagaku

admin.site.register(Yoyaku)
admin.site.register(Room)
admin.site.register(Plan)
admin.site.register(Calendar)
admin.site.register(Sagaku)