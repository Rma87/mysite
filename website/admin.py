from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'email', 'created_date')
    empty_value_display = '-empty-'
    list_filter = ('created_date', 'email')
    search_fields = ['name', 'email', 'email']
    
admin.site.register(Contact, ContactAdmin)
