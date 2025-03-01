from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from tracker.serializers.category_serializers import CategorySerializer
from tracker.services import CategoryService


class CategoryListCreateAPIView(APIView):
    serializer_class = CategorySerializer
    service = CategoryService()
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        categories = self.service.all()
        paginator = self.pagination_class()
        paginated_categories = paginator.paginate_queryset(categories,request,view=self)
        serializer = self.serializer_class(paginated_categories, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.service.create(serializer.validated_data)
        serializer = self.serializer_class(instance)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class CategoryRetrieveUpdateDestroyAPIView(APIView):
    serializer_class = CategorySerializer
    service = CategoryService()

    def get(self, request, *args, **kwargs):
        category_id = kwargs.get("category_id")
        category = self.service.get(id=category_id)
        serializer = self.serializer_class(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        category_id = kwargs.get("category_id")
        category = self.service.get(id=category_id)
        serializer = self.serializer_class(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.service.update(category, serializer.validated_data, **kwargs)
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        category_id = kwargs.get("category_id")
        category = self.service.get(id=category_id)
        if not category:
            return Response({"detail":"category not found!"},status=status.HTTP_404_NOT_FOUND)
        self.service.delete(category)
        return Response({"detail": "Category Deleted Successfully."},status=status.HTTP_204_NO_CONTENT)


