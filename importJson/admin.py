from django.contrib import admin
from .models import RetreivedData
from django.core import management
from django.shortcuts import redirect

class RetreivedDataAdmin(admin.ModelAdmin):

    def import_data_from_url(self, request):
        print('import data here')
        try:
            management.call_command('import_from_url')
            message = 'successfully imported data from URL'

        except Exception as ex:
            message = 'Error importing from data from URL {}'.format(str(ex))

        admin.ModelAdmin.message_user(RetreivedData, request, message)
        return redirect('admin:index')

admin.site.register(RetreivedData, RetreivedDataAdmin)