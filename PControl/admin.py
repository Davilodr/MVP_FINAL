from django.contrib import admin

from .models import Dias_trabajados, Horas_trabajadas, PersonalCC, PersonalDXTV, Supervisor

# Register your models here.

admin.site.register(PersonalCC)
admin.site.register(PersonalDXTV)
admin.site.register(Dias_trabajados)
admin.site.register(Horas_trabajadas)
admin.site.register(Supervisor)