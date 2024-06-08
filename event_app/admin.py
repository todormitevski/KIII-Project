from django.contrib import admin

from event_app.models import *


# Register your models here.


class EventBandInline(admin.TabularInline):
    model = EventBand
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [EventBandInline,]
    list_display = ['name', 'datetime',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


class BandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country',]


admin.site.register(Event, EventAdmin)
admin.site.register(EventBand)
admin.site.register(Band, BandAdmin)
