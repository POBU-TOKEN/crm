from django.contrib.admin import SimpleListFilter
from .models import Contact


class ContactFilter(SimpleListFilter):
    title = "Contact"
    parameter_name = 'contact'

    def lookups(self, request, model_admin):
        contacts = Contact.objects.filter(user=request.user).values_list('id', 'name')
        return contacts
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contact__id=self.value())
        return queryset.filter(contact__user=request.user)
