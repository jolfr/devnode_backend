from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from .auth import google_authenticate
import json

import logging
logger = logging.getLogger(__name__)


CLIENT_ID = '462887418296-9a67ol2li3j8nr918im4m9rjejmsommn.apps.googleusercontent.com'

# Create your views here.


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    logger.error('Content Params')
    logger.error(request.content_params.__str__())
    logger.error('Content Type')
    logger.error(request.content_type)
    logger.error('Encoding')
    logger.error(request.encoding)
    logger.error('Path')
    logger.error(request.path)
    logger.error('Body')
    logger.error(request.body.__str__())
    # user_token = request.POST.get("user_token")

    req = json.loads(request.body)

    user_token = req['user_token']

    logger.error('User Token:')
    logger.error(user_token)

    session_token = google_authenticate(user_token)

    return Response({'session_token': session_token},
                    status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def logout(request):
    # simply delete the token to force a login
    request.user.auth_token.delete()
    return Response(status=HTTP_200_OK)
