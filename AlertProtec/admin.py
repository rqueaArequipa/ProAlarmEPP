from django.contrib import admin

from .models import Machinery, Person, User, Alert, Device

#admin.site.register(Machinery)
#admin.site.register(Person)
#admin.site.register(User)
#admin.site.register(Alert)
#admin.site.register(Device)

@admin.register(Machinery)
class MachineryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_machinery','model', 'num_serial', 'year', 'capacity', 'type_fuel', 'hour', 'date_maintenance', 'status', 'type_engine', 'img')
    search_fields = ('status',)
    list_display_links = ('type_machinery',)
    list_filter = ('status',)
    list_per_page = 8

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'dni', 'number', 'email', 'date_birth', 'address', 'certifications', 'machinery')
    search_fields = ('dni',)
    list_editable = ('machinery',)
    list_display_links = ('name',)
    list_per_page = 8
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'person', 'rol', 'date_created', 'avatar')
    search_fields = ('username', )
    list_display_links = ('username',)
    list_filter = ('rol',)
    list_per_page = 8

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'person')
    search_fields = ('status',)
    list_display_links = ('person',)
    list_filter = ('status',)
    list_per_page = 8

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'token')
    list_per_page = 8
    exclude = ('token', )
