from django.contrib.admin import ModelAdmin, register
from django.utils.translation import gettext_lazy as _
from core.models import Data


# Register your models here.
@register(Data)
class DataAdmin(ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'username', 'password')
    search_fields = ('id', 'username', 'password')
    ordering = ('id',)

    fieldsets = (
        (
            _('Information'),
            {
                'fields': (
                    'username',
                    'password'
                )
            }
        ),
    )
