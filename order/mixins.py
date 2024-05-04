from django.forms import modelformset_factory
from django.http import JsonResponse


class DynamicFormsetMixin:
    model = None
    form_class = None
    extra_forms = 0

    def setup_formset(request):
        print(request)
