from django.contrib import admin
from .models import MailingSettings, MailingMessage


class MailingSettingsInline(admin.StackedInline):
    model = MailingSettings
    extra = 1
    can_delete = False
    verbose_name = 'Mailing Setting'
    verbose_name_plural = 'Mailing Setting'


@admin.register(MailingMessage)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('subject', 'owner',)
    list_filter = ('owner',)
    inlines = [
        MailingSettingsInline,
    ]
