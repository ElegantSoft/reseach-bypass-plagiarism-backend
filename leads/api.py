from rest_framework.decorators import action, api_view, parser_classes

from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .converter import Converter


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

    # @api_view(['GET'])
    @action(detail=False, methods=['POST'], name='Test router')
    @parser_classes(JSONParser,)
    def test(self, request, *args, **kwargs):
        return Response(Converter.convert(request.data['content']))