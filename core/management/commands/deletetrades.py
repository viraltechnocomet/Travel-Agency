from django.core.management.base import BaseCommand
from core.models import TradeSignal
import datetime


# crotab :  0 0 * * * ~/TradeCopier/venv/bin/python ~/TradeCopier/manage.py deletetrades
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        time_threshold = datetime.datetime.now() - datetime.timedelta(hours=6)
        signals_queryset = TradeSignal.objects.filter(signal_time__lt=time_threshold)
        signals_queryset.delete()
