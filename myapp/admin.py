from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_email','doc_name','booking_date','doc_name','booking_date','booked_on')
admin.site.register(booking,BookingAdmin)
