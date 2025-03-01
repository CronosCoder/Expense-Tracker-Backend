from core.services import BaseModelService
from tracker.models import Transaction


class TransactionService(BaseModelService):
    model_class = Transaction