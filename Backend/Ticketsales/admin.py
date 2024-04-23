from django.contrib import admin # type: ignore




from .models import ConcertModel , LocationModel , TicketModel , ProfileModel , TimeModel

# Register your models here.



admin.site.register(ConcertModel)
admin.site.register(LocationModel)
admin.site.register(ProfileModel)
admin.site.register(TicketModel)
admin.site.register(TimeModel)