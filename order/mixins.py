import json
from django.db import transaction
from django.http import JsonResponse


class JsonDeserializerMixin:
    model = None

    def deserialize_json_with_parent_and_children(self, **kwargs):
        try:
            with transaction.atomic():
                json_data = kwargs.get("json_data", None)

                if json_data:
                    parent_key = kwargs.get("parent_key")
                    parent_model = kwargs.get("parent_model")
                    child_key = kwargs.get("child_key")
                    child_model = kwargs.get("child_model")
                    child_relation_attr = kwargs.get("child_relation_attr")

                    parent_instances = []
                    for parent_instance_data in json_data[parent_key]:
                        parent_instance, created = (
                            parent_model.objects.update_or_create(
                                id=parent_instance_data.get("id"),
                                defaults={**parent_instance_data},
                            )
                        )

                        parent_instances.append(parent_instance)

                        child_instances = []
                        for child_instance_data in parent_instance[child_key]:
                            child_instance_data[child_relation_attr] = (
                                parent_instance  # Set FK to the parent instance
                            )
                            child = child_model(**child_instance_data)
                            child_instances.append(child)

                        if child_instances:
                            child_model.objects.bulk_create(child_instances)

                else:
                    NotImplementedError("json data was empty")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
