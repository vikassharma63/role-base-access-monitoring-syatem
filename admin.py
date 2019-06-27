from django.contrib import admin
from users.models import System,Module,Logs,Daily
# Register your models here.
admin.site.register(Logs)
admin.site.register(System)
admin.site.register(Module)
admin.site.register(Daily)
