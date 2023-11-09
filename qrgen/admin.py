from django.contrib import admin

# Register your models here.
from qrgen.models import Qrgen

class QrgenAdmin(admin.ModelAdmin):
    pass

admin.site.register(Qrgen, QrgenAdmin)