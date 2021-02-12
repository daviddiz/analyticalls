from django.db import models



class RetreivedData(models.Model):
    """
    Data retrieved from json source
    """

    id = models.AutoField(primary_key=True)

    symbol = models.CharField(max_length=12)
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()
    quoteVolume = models.FloatField()
    percentChange = models.FloatField()
    updatedAt = models.DateTimeField(null=True, blank=True)


    """def __init__(self, *args, **kwargs):
        super(RetreivedData, self).__init__(*args, **kwargs)
        self._source_obj = None"""