from rest_framework.generics import get_object_or_404


class BaseModelService:
    model_class = None

    def prepare_data(self, validated_data):
        return validated_data

    def get_model_class(self):
        assert self.model_class is not None, (
            "%s should include mode_class attribute" % self.__class__.__name__
        )
        return self.model_class

    def create(self, validated_data, **kwargs):
        validated_data = self.prepare_data(validated_data)
        model_class = self.get_model_class()
        instance = model_class.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data, **kwargs):
        validated_data = self.prepare_data(validated_data)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def get(self, **kwargs):
        model_class = self.get_model_class()
        instance = get_object_or_404(model_class, **kwargs)
        return instance

    def all(self, **kwargs):
        model_class = self.get_model_class()
        instances = model_class.objects.filter(**kwargs)
        return instances

    def get_or_create(self, **kwargs):
        model_class = self.get_model_class()
        created, instance = model_class.objects.get_or_create(**kwargs)
        return created, instance


