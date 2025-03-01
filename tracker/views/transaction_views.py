from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.serializers.transaction_serializers import TransactionSerializer, TransactionDetailSerializer
from tracker.services import TransactionService


class TransactionListCreateAPIView(APIView):
    serializer_class = TransactionSerializer
    detail_serializer_class = TransactionDetailSerializer
    service = TransactionService()
    pagination_class = LimitOffsetPagination

    def get(self,request, *args, **kwargs):
        transactions = self.service.all()
        paginator = self.pagination_class()
        paginated_transactions = paginator.paginate_queryset(transactions, request)
        serializer = self.detail_serializer_class(paginated_transactions, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.service.create(serializer.validated_data)
        return Response(self.detail_serializer_class(instance).data)


