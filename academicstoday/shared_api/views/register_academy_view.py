import django_filters
import django_rq
from starterkit.drf.permissions import IsAuthenticatedAndIsActivePermission
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import mixins # See: http://www.django-rest-framework.org/api-guide/generic-views/#mixins
from rest_framework import authentication, viewsets, permissions, status, parsers, renderers
from rest_framework.decorators import detail_route, list_route # See: http://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
from rest_framework.response import Response
from shared_foundation import models
from shared_foundation import utils
from shared_academy.tasks import create_academy_func
from shared_api.serializers.register_academy_serializers import RegisterAcademySerializer


class RegisterAcademyAPIView(APIView):
    throttle_classes = ()
    permission_classes = (
        permissions.IsAuthenticated,
        IsAuthenticatedAndIsActivePermission,
    )
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        # Perform validation.
        serializer = RegisterAcademySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Attempt to create a user and return status.
        try:
            # Send an email.
            django_rq.enqueue(
                create_academy_func,
                {
                    'user_pk': request.user.id,
                    'schema_name': serializer.validated_data['schema_name'],
                    'name': serializer.validated_data['name'],
                    'alternate_name': serializer.validated_data['alternate_name']
                }
            )

            # Implemented response.
            return Response({
                'status': 'Registered',
                'reason': ''
            })
        except Exception as e:
            return Response({
                'status': 'Failed',
                'reason': str(e)
            })
