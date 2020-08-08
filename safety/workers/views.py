# # # # # # # # # # before use rest framework # # # # # #
# import json

# from django.views import View
# from django.http import HttpResponse
# from django.shortcuts import render

# from .models import Worker

# # class-base view


# class WorkerListView(View):

#     def get(self, request):

#         workers = Worker.objects.all()

#         # return sample html
#         html = ''
#         for worker in workers:
#             html += f'<li>{worker.first_name}</li>'
#         return HttpResponse(html)

#         # rendor html file and passing context
#         worker_list = []
#         for worker in workers:
#             worker_list.append(worker.first_name)
#         return render(
#             request,
#             'worker_list.html',
#             {'workers': worker_list},
#         )

#         return render(
#             request,
#             'worker_list.html',
#             {'workers': workers}
#         )

#         worker_list = []
#         for worker in workers:
#             model = {
#                 "first_name": worker.first_name,
#                 "last_name": worker.last_name,
#                 "is_available": worker.is_available,
#                 "primary_phone": worker.primary_phone,
#                 "secondary_phone": worker.secondary_phone,
#                 "address": worker.address,
#             }
#             worker_list.append(model)
#         return HttpResponse(
#             json.dumps(worker_list),
#             content_type='application/json'
#         )
# # # # # # # # # # end before use rest framework # # # # # #

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import viewsets

from .models import Worker
from .serializers import WorkerSerializer


class WorkerListView(APIView):
    def get(self, request, format=None):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

# class WorkerModelViewSet(viewsets.ModelViewSet):
#      serializer_class = WorkerSerializer
#      queryset = Worker.objects.all()
