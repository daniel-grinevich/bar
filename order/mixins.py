from recipe.models import Menu


class TicketHtmxFormMixin:
    def setup_formset(self, **kwargs):
        request = kwargs.get("request")
        keys = kwargs.get("keys", [])

        # Prepare data dict for formset initialization
        formset_data = {
            "form-TOTAL_FORMS": "0",  # This will be updated
            "form-INITIAL_FORMS": "0",
            "form-MAX_NUM_FORMS": "",
        }

        # Assuming keys contain names of the fields expected in each form of the formset
        total_forms = 0
        for key in keys:
            values = request.POST.getlist(key)
            total_forms = len(values)  # Assuming all lists are of the same length
            for i, value in enumerate(values):
                formset_data[f"{kwargs.get('formset_string')}-{i}-{key}"] = value

        formset_data["form-TOTAL_FORMS"] = str(total_forms)

        # Now, initialize the formset with the prepared data
        formset = formset_data

        return formset

    def initialize_formset_htmx(self, **kwargs):
        formset = kwargs["formset"]
        fields = set()

        # Iterate over each form in the formset
        for form in formset:
            # Collect the fields for each form
            for field_name, field in form.fields.items():
                fields.add(field_name)

        # Optionally, convert the set to a list if needed
        fields_list = list(fields)

        print("Formset fields:", fields_list)

        return fields_list


class MenuItemMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_id = kwargs.get("request").GET.get("menu_id", None)

        # book = Book.objects.get(title='Example Book')
        # authors = book.authors.all()
        menu = Menu.objects.get(id=menu_id)
        context["menu_items"] = menu.items.all()
