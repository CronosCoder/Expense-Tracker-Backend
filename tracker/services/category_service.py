from django.db import transaction

from core.services import BaseModelService
from tracker.models import Category


class CategoryService(BaseModelService):
    model_class = Category

    @transaction.atomic
    def delete(self, instance):
        instance.delete()
        return True