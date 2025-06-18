from typing import Any
from django.contrib import admin
from account.models import User, Contact, Activity

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email')
    fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'phone', 'email', 'company')
    list_display = ('name', 'surname', 'phone', 'email', 'company', 'user')
    search_fields = ('name', )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fields = ('name', 'activity_type', 'description')