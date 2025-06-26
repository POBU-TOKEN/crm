from typing import Any
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db.models.query import QuerySet
from account.models import User, Contact, Activity

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

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'password')
    list_display = ('username', 'email', 'first_name', 'last_name')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'phone', 'email', 'company')
    list_display = ('name', 'surname', 'phone', 'email', 'company', 'user__username')
    search_fields = ('name', )

    def get_queryset(self, request):
        user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fields = ('name', 'activity_type', 'description', 'contact')
    list_display = ('name', 'activity_type', 'description', 'contact')
    list_filter = (ContactFilter, 'activity_type', )
    raw_id_fields = ('contact', )
