from rest_framework.viewsets import ModelViewSet

from .serializers import CertificateModelSerializer
from .models import Certificate


class CertificateModelViewSetView(ModelViewSet):
    serializer_class = CertificateModelSerializer
    queryset = Certificate.objects.all()
