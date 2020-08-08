from django.views import View
from django.http import HttpResponse

import requests

class Covid19ReportView(View):
    def get(self, request):
        response = requests.get('https://covid19.th-stat.com/api/open/today')
        data = response.json()
        new_confirm = data['NewConfirmed']
        
        return HttpResponse(f'NewConfirmed: {new_confirm}')
        
    