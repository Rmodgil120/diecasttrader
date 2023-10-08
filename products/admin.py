from django.contrib import admin
from .models import hotwheels, tomica, maisto, majorette, mathchbox, others

class hotwheelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'email_id', 'number')

class tomicaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'email_id', 'number')

class masitoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'email_id', 'number')

class majoretteAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'email_id', 'number')

class matchboxAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'email_id', 'number')

class othersAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'email_id', 'number')

# Register your models here.

admin.site.register(others, othersAdmin)
admin.site.register(maisto, masitoAdmin)
admin.site.register(hotwheels, hotwheelsAdmin)
admin.site.register(tomica, tomicaAdmin)
admin.site.register(majorette, majoretteAdmin)
admin.site.register(mathchbox, matchboxAdmin)