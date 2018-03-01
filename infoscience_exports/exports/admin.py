from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.options import ModelAdmin

from django_tequila.admin import TequilaAdminSite

from log_utils import LoggedModelAdminMixin
from .models import Export, User


admin.autodiscover()
admin.site.__class__ = TequilaAdminSite


class EPFLUserModelAdmin(UserAdmin):
    list_display = ('username', 'email', 'sciper', 'last_login', 'is_superuser')


class ExportLoggedModelAdmin(LoggedModelAdminMixin, ModelAdmin):
    list_display = ('name', 'user', 'updated_at')
    list_filter = ('updated_at', )


admin.site.register(Export, ExportLoggedModelAdmin)
admin.site.register(User, EPFLUserModelAdmin)
