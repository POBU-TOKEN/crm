from django.contrib.contenttypes.models import ContentType


class SeeLogButtonMixin:
    change_list_template = 'audit_button_change_list.html'

    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}

        # Get content_type of current model
        model_content_type = ContentType.objects.get_for_model(self.model)
        extra_context['model_content_type_id'] = model_content_type.id
        extra_context['model_verbose_name'] = self.model._meta.verbose_name.capitalize()

        extra_context['model_app_label'] = self.model._meta.app_label
        extra_context['model_model_name'] = self.model._meta.model_name

        return super().changelist_view(request, extra_context=extra_context)
