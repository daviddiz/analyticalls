"""
Import json data from URL to Datababse
"""
import requests
import json
from importJson.models import RetreivedData
from django.core.management.base import BaseCommand
from datetime import datetime
from time import time, sleep

IMPORT_URL = 'https://api.bittrex.com/v3/markets/BTC-USDT/summary'


class Command(BaseCommand):
    def import_data(self, data):
        print(data)
        symbol = data.get('symbol', None)
        high = data.get('high', None)
        low = data.get('low', None)
        volume = data.get('volume', None)
        quoteVolume = data.get('quoteVolume', None)
        percentChange = data.get('percentChange', None)
        updatedAt = data.get('updatedAt', None)

        try:
            indata, created = RetreivedData.objects.get_or_create(
                symbol=symbol,
                high=high,
                low=low,
                volume=volume,
                quoteVolume=quoteVolume,
                percentChange=percentChange,
                updatedAt=updatedAt
            )
            if created:
                indata.save()
                display_format = "\nData, {}, has been saved."
                print(display_format.format(indata))
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this data: {}\n{}".format(updatedAt, str(ex))
            print(msg)


    def handle(self, *args, **options):
        """
        Makes a GET request to the  API every minute.
        """
        

        while True:
            sleep(60 - time() % 60)
        
            headers = {'Content-Type': 'application/json'}
            response = requests.get(
                url=IMPORT_URL,
                headers=headers,
            )
    
            response.raise_for_status()
            data = response.json()
            self.import_data(data)

        """for data_object in data:
            self.import_data(data_object)"""
