from django.urls import path

from tracker.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("api/v1/categories/", CategoryListCreateAPIView.as_view(), name="category_list_create"),
    path("api/v1/categories/<int:category_id>/", CategoryRetrieveUpdateDestroyAPIView.as_view(),
         name="category_retrieve_update_destroy"),
]
